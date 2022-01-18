import re
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

message_regex = re.compile(r"^\[(\d{1,2}\.\d{1,2}\.\d{4}\,\s\d{2}\:\d{2})\]\s([\w\s]+)\:\s(.+)$")

message_data_frames = []

with open("./messages.txt") as chat_log:
    for message in chat_log:
        result = re.search(message_regex, message)
        if result:
            datetime = pd.to_datetime(result.group(1), format='%d.%m.%Y, %H:%M')
            message_data_frames.append(
                pd.DataFrame(
                    {
                        "datetime": [datetime],
                        "sender": [result.group(2)],
                        "message": [result.group(3)]
                    }
                )
            )



chat_data_frame = pd.concat(message_data_frames)
chat_data_frame["weekday"] = chat_data_frame["datetime"].apply(lambda date: date.strftime("%A"))
chat_data_frame["hour_of_the_day"] = chat_data_frame["datetime"].apply(lambda date: date.hour)

plt.close("all")
chat_data_frame['sender'].value_counts(sort=False).plot.pie()
plt.show()
