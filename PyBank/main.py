import os
import csv

csvpath = os.path.join(os.path.abspath(__file__),'..','Resources','budget_data.csv')

months = []
profitlist = []
profitvloss = 0
MinProfitIndex = 0
MaxProfitIndex = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        months = months + [row[0]]
        profitvloss = profitvloss + float(row[1])
        profitlist = profitlist + [row[1]]
        
        
countofmonths = len(months)
countofprofit = len(profitlist)
averageprofit = profitvloss / countofprofit
print(countofmonths)
print(profitvloss)
print(averageprofit)




#Loop through months and make a list
#Count months in this list
#Add up totals from profit column
#Loop trought profit column and make a list
#find max and min in list
# Index location with a variable for each
# use variable to look up month from month list
# print out a nice output in terminal and a text file



