import re
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

class MessageFormatter:

    message_regex = re.compile(r"^\[(\d{1,2}\.\d{1,2}\.\d{4}\,\s\d{2}\:\d{2})\]\s([\w\s]+)\:\s(.+)$")

    @staticmethod
    def chat_to_data_frame(chat):
        data = []
        for message in chat:
            result = re.search(MessageFormatter.message_regex, message)
            if result:
                datetime = pd.to_datetime(result.group(1), format='%d.%m.%Y, %H:%M')
                sender = result.group(2)
                message = result.group(3)
                data.append([datetime, sender, message])

        return pd.DataFrame(data, columns=['datetime', 'sender', 'message'])

class ChartPlotter:

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    @staticmethod
    def plot_weekly_distribution_bar_chart(dataset):
        data_set = chat_data_frame['weekday'].value_counts(sort=False).reindex(range(7), fill_value=0).sort_index()
        data_set.plot(kind="bar")
        plt.xticks(range(7), ChartPlotter.weekdays)
        plt.show()

    @staticmethod
    def plot_message_share_pie_chart(dataset):
        data_set = chat_data_frame['sender'].value_counts(sort=False)
        data_set.plot(kind="pie")
        plt.show()

    @staticmethod
    def plot_hourly_distribution_bar_chart(dataset):
        data_set = chat_data_frame['hour_of_the_day'].value_counts(sort=False).reindex(range(24), fill_value=0).sort_index()
        data_set.plot(kind="bar")
        plt.show()



def generate_derived_columns(data_frame):
    data_frame["weekday"] = chat_data_frame["datetime"].apply(lambda date: date.weekday())
    data_frame["hour_of_the_day"] = chat_data_frame["datetime"].apply(lambda date: date.hour)


with open("./messages.txt") as chat_log:
    chat_data_frame = MessageFormatter.chat_to_data_frame(chat_log)
    generate_derived_columns(chat_data_frame)
    ChartPlotter.plot_weekly_distribution_bar_chart(chat_data_frame)
    ChartPlotter.plot_message_share_pie_chart(chat_data_frame)
    ChartPlotter.plot_hourly_distribution_bar_chart(chat_data_frame)
