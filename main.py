import csv
import pandas
from numpy import double

# # Challenge 1 is to open the csv file and read data into a list in a Traditional way
# # with open ("weather_data.csv") as file:
# #     weather_data = file.readlines()
# #     print(weather_data)
#
# # Challenge 2 is to open the csv file and read data row wise using csv package
# # with open ("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         print (row)
# #     # Challenge 3 is to store and return all the temperature values into a list as int.
# #         # print (column[1])
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# # Challange 4 is to read the csv data using pandas library and print temp column data.
# data = pandas.read_csv("weather_data.csv")  #Data Frame
# # print(data)
# # print(data["temp"])
# # print(type(data))
# # print(type(data["temp"]))
#
# # Challenge 5 is to store data of temp column into a list and calculate average temperature using pandas.
# temp_data = data["temp"]    #Series
# temp_list = temp_data.to_list()
# avg_temp = 0
# # Without using Mean
# for i in temp_list:
#     avg_temp += int(i)
# avg_temp /= len(temp_list)
# # print(round(avg_temp,2))
# # With Using Mean
# # print(temp_data.mean())
#
# # Challenge 6 is to return the largest value of the Temp Column.
# # print(temp_data.max())
#
# # Challenge 7 is to return the row data of max temperature value.
# # print(data[data.temp == temp_data.max()])
#
# # Challenge 8 is to get the Temperature data of Monday and convert it into Celsius.
# temp_monday = data[data.day == "Monday"].temp
# print (((temp_monday*9/5)+32).iloc[0])
#
# # Challenge 9 is to create a DataFrame from Scratch.
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data_frame = pandas.DataFrame(data_dict)    # Create a Data frame using DataFrame class of Pandas Library.
# data_frame.to_csv("new_dataframe.csv")  # Writing the created Dataframe into a new CSV File.

# Create a Data Frame for the given CSV Data.
dataframe_1 = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(dataframe_1)
# My Approach: Used Series functions like unique and value_counts to display data.
color_series = dataframe_1["Primary Fur Color"]
unique_colors = color_series.unique()
# print(color_series.value_counts())

# Course Approach: Read each value and get counts of each value and then declare a data_dictionary and from that to create a Data frame and then a CSV File.
count_list = []
for i in unique_colors:
    count = len(dataframe_1[dataframe_1["Primary Fur Color"] == i])
    count_list.append(count)

data_dict_1 = {
    "Color" : unique_colors,
     "Count" : count_list
}
data_frame_2 = pandas.DataFrame(data_dict_1)
data_frame_2.to_csv("Count_Squirrel_ByColor.csv")


