#import the os module
import os

#import module for reading csv
import csv

csvpath=os.path.join('.','Resources','budget_data.csv')

#Lists to store data
Total_months=0
Total = []


#Reading file using csv module
with open(csvpath, encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile , delimiter=',')
    print(csvreader)


    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        #print(row)
        Total.append(int(row[1]))
        
        #Add number of months
        Total_months+=1
        Total_PL = sum(Total)
      
    
print("Total Months: " + str(Total_months))
print(Total_PL)


