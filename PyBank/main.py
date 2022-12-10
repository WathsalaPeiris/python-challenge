#import the os module
import os

#import module for reading csv
import csv

#specify the path to the csv file
csvpath=os.path.join('.','Resources','budget_data.csv')

#Lists to store data from csv
Total = []
Diff_Total = []
Month = []

#Set variable to count number of months
Total_months=0

#Open and Read file using csv module
with open(csvpath, encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile , delimiter=',')
    
    #read the Header row first
    csv_header = next(csvreader)
  
    #Read through each row after the Header
    for row in csvreader:
        #Assign Column 2 data in List named Total
        Total.append(int(row[1]))
        
        #Assign Column 1 data in List named Month
        Month.append(row[0])
        
        #Keep counting  number of months
        Total_months+=1
        
        #Assign the Sum of the Column 2 Data in a Variable named Total_PL
        Total_PL = sum(Total)
        
    #Define a range starting from 1 to length of Column 2 data   
    Total_Length = range(1,len(Total))

    #Go throgh each value of Column 2
    for i in Total_Length:
       
        #From each row value, subtract the upper row value in Column 2
        k=int(Total[i]) - int(Total[i-1])
      
        #Append all the differences in the List named Diff_Total
        Diff_Total.append(int(k))

    #Set variables to store the starting point to find Greatest and Lowest difference - first Value of Difference List and Second Value in Month List
    High_PL = int(Diff_Total [0])
    High_M = Month[1]
    Low_PL = int(Diff_Total [0])
    Low_M = Month[1]
    
    #Define a range starting from 1 to length of List of Differences
    Diff_Total_Length = range(1,len(Diff_Total))

    #Go through each value in List of Differences
    for j in Diff_Total_Length:

        #If a value in Differnce List is greater than High_PL, replace the High_PL value by the relevant Differnce
         if int(Diff_Total[j]) > High_PL:
            High_PL = int(Diff_Total[j])
            #Replace the High_M value by relevant month
            High_M = Month[j+1]
   
        #If a value in Differnce List is lower than Low_PL, replace the Low_PL value by the relevant Differnce
         if int(Diff_Total[j]) < Low_PL:
            Low_PL = int(Diff_Total[j])
            #Replace the Low_M value by relevant month
            Low_M = Month[j+1]

   
#Print Title
print("Financial Analysis")

print("-----------------------------------")

#Print Total number of months
print("Total Months: " + str(Total_months))

#Print the Sum of the Profit/Loss Column
print("Total: $"+str(Total_PL))

#Calculate and round the average of differences and then print the average of differences
print("Average Change: $" + str( round((sum(Diff_Total)/len(Diff_Total)),2)))

#Print the month and value of the greatest increase in profits
print(f"Greatest Increase in Profits:  {High_M} (${High_PL})")

#Print the month and value of the greatest decrease in profits
print(f"Greatest Decrease in Profits:  {Low_M} (${Low_PL})\n")

# Print the Analysis in a text file
file_name = "PyBank_Analysis.txt"
file_path = os.path.join('.','Analysis',file_name)

with open(file_path,"w") as f:
    
    f.write("Financial Analysis\n\n")

    f.write("-----------------------------------\n\n")

    f.write(f"Total Months: {Total_months}\n\n")

    f.write("Total: $"+str(Total_PL)+'\n \n')

    f.write("Average Change: $" + str( round((sum(Diff_Total)/len(Diff_Total)),2)) + '\n\n')

    f.write(f"Greatest Increase in Profits:  {High_M} (${High_PL}) \n\n")

    f.write(f"Greatest Decrease in Profits:  {Low_M} (${Low_PL})\n\n")

#Print a messeage in the Terminal
print('PyBank_Analysis.txt file was created in Analysis Folder')

