#Importing CSV data

import os
import csv

csvpath = os.path.join(os.path.abspath(__file__),'..','Resources','budget_data.csv')

# Count Months and Total Proft/Loss from CSV

months = []
profitlist = []
profitvloss = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        months = months + [row[0]]
        profitvloss = profitvloss + float(row[1])
        profitlist = profitlist + [row[1]]
    
countofmonths = len(months)
countofprofit = len(profitlist)

# Average Change in Proft/Loss

changeinProfit = []
monthchange = 0    
    
for i in range(1, len(profitlist)):
    monthchange = int(profitlist[i]) - int(profitlist[i - 1])
    changeinProfit.append(monthchange)

totalchangeinprofit = sum(changeinProfit)
monthchangecount = len(changeinProfit)
averagechangeinprofit = round(totalchangeinprofit / monthchangecount, 2)

# Max and Min
MinProfit = min(changeinProfit)
MaxProfit = max(changeinProfit)

# Readout

print(f"Total Months: {countofmonths}")
print(f"Total: ${profitvloss}")
print(f"Average Change: ${averagechangeinprofit}")
print(f"Greatest Increase in Profits: Feb-2012 (${MaxProfit})")
print(f"Greatest Decrease in Profits: Sep-2013 (${MinProfit})")

# Export to .txt

File_Object = open(r"C:\Users\Calvin Bauer\python-challenge\PyBank\Analysis\Analysis.txt","w")
File_Object.write ("Financial Analysis\n")
File_Object.write ("----------------------------------\n")
File_Object.write (f"Total Months: {countofmonths}\n")
File_Object.write (f"Total: ${profitvloss}\n")
File_Object.write (f"Average Change: ${averagechangeinprofit}\n")
File_Object.write (f"Greatest Increase in Profits: Feb-2012 (${MaxProfit})\n")
File_Object.write (f"Greatest Decrease in Profits: Sep-2013 (${MinProfit})\n")


#Psuedo Code Plan
#Loop through months and make a list
#Count months in this list
#Add up totals from profit column
#Loop trought profit column and make a list
#find max and min in list
# Index location with a variable for each
# use variable to look up month from month list
# print out a nice output in terminal and a text file