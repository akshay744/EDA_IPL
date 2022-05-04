from pydoc import describe
from turtle import color
from unittest import result
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

#eda on ipl data
#importing csv file using pandas 
ipl=pd.read_csv('ipl.csv')
print(ipl)

#use head to find top 5 rows
top5 = ipl.head()
print(top5)

#to find number of rows and columns
row_columns = ipl.shape
print(row_columns)

#to find the count of the man of the match won by players
count = ipl['ManOfMach'].value_counts()
print(count)

#top 5 players
count5 = list(ipl['ManOfMach'].value_counts()[0:5].keys())
print(count5)

#bar graph of top 5 players 
plt.figure(figsize=(8,5))
plt.bar(list(ipl['ManOfMach'].value_counts()[0:5].keys()),list(ipl['ManOfMach'].value_counts()[0:5]), color='g')
plt.show()

#getting frequency of result column
result = ipl['Outcome_Type'].value_counts()
print(result)

#getting the count of toss wining w.r.t teams
toss = ipl['Outcome_Type'].value_counts()
print(toss)

#getting the list of teams winning by first batting
batting_first= ipl[ipl['Win_Type']!='wickets'] 
print(batting_first)

#ploting histogram of above data for histogram we need numerical values that's why we cant plot histogram in this case as it is in string datatype
plt.figure(figsize=(5,7))
plt.hist(batting_first['Win_Type'])
plt.xlabel('Runs')
plt.show()

#who win most matches by batting first
win_first = batting_first['match_winner'].value_counts()
print(win_first)

#to check datatypes of columns
types = ipl.dtypes

#bar grapgh
plt.figure(figsize=(6,6))
plt.bar(list(batting_first['match_winner'].value_counts()[0:3].keys()),list(batting_first['match_winner'].value_counts()[0:3]),color=["red","green","blue"])
plt.show()

#pie chart
plt.figure(figsize=(5,7))
plt.pie(list(batting_first['match_winner'].value_counts()),labels=list(batting_first['match_winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()

#second batting
batting_second= ipl[ipl['Win_Type']!='runs'] 
top_5 = batting_second.head()
print(top_5)

#ploting histogram of above data for histogram we need numerical values that's why we cant plot histogram in this case as it is in string datatype
plt.figure(figsize=(7,7))
plt.hist(batting_second['Win_Type'],bins=30)
plt.show()

#second batting count of winning match w.r.t team
second_win = batting_second['match_winner'].value_counts()
print(second_win)

#bar graph
plt.figure(figsize=(5,6))
plt.bar(list(batting_second['match_winner'].value_counts()[0:3].keys()),list(batting_second['match_winner'].value_counts()[0:3]),color=["red","green","blue"])
plt.show()

#pie chart
plt.figure(figsize=(5,5))
plt.pie(list(batting_second['match_winner'].value_counts()),labels=list(batting_second['match_winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()

#number of matches played every season
matches = ipl['Season_Year'].value_counts()
print(matches)

#number of matches played in cities
cities = ipl['City_Name'].value_counts()
print(cities)

#how many times teams wins matches when they win toss
tosswin_matchwin = np.sum(ipl['Toss_Winner']==ipl['match_winner'])
print(tosswin_matchwin)

#percentage of above 
ratio = 324/637
print(ratio)

#to calculate total entries in particular column
match_id = sum(ipl['match_id'].value_counts())
print(match_id)

