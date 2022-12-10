#import the os module
import os

#import module for reading csv
import csv

#specify the path to the csv file
csvpath=os.path.join('.','Resources','election_data.csv')

#Lists to store data from csv
Candidate = []
Candit_Name = []

#Set variable to count number of votes
Num_votes=0

#Open and Read file using csv module
with open(csvpath, encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile , delimiter=',')
    
    #read the Header row first
    csv_header = next(csvreader)
  
    #Read through each row after the Header
    for row in csvreader:
        #Assign Column 3 data in List named Candit_Name
        Candidate.append(row[2])
        

        #Keep counting number of votes
        Num_votes+=1
        
    #Sort the Values in Candidate List
    Candidate.sort()
    
    #Append the first value from Candidate list in to Candit_Name list
    Candit_Name.append(Candidate[0])
    
    
    #Set ranges to iteartes through Candidate list
    Length_votes = range(1,len(Candidate))
    
    #Set ranges to iteartes through Candidate list and Candit_Name list
    Len_Votes = range(len(Candidate))

    #Append the remaining unique values from Candidate list into Candit_Name list
    for i in Length_votes:
        if Candidate[i]!=Candidate[i-1]:
            Candit_Name.append(Candidate[i])

    #Check how many Candidates are there
    print("There are " + str(int(len(Candit_Name))) + " candidates in the data set" + "\n\n")
    
    #Set variables to count votes for each Candidate seperately
    Candit1=0
    Candit2=0
    Candit3=0

    for i in Len_Votes:
        
        if Candidate[i]==Candit_Name[0]:
            Candit1+=1
    
        if Candidate[i]==Candit_Name[1]:
            Candit2+=1

        if Candidate[i]==Candit_Name[2]:
            Candit3+=1

#Set variables to store Percentage votes
Percent1= (Candit1 / Num_votes)
Percent2= (Candit2 / Num_votes)
Percent3= (Candit3 / Num_votes)

#Set a dictoinary to store Candidate names and votes
Cand = {"Name": [Candit_Name[0],Candit_Name[1],Candit_Name[2]],
        "Votes": [Candit1, Candit2, Candit3]}

#Set variable to store winner name
Winner = Cand["Name"][0]

#Compare the number of votes and replace the winner name
if Cand["Votes"][1] > Cand["Votes"][0]:
    Winner = Cand["Name"][1]

    if Cand["Votes"][2] > Cand["Votes"][1]:
        Winner = Cand["Name"][2]



#Print results in the Terminal
print("Election Results\n")

print("----------------------------\n")

print("Total Votes: " + str(int(Num_votes)) + "\n")

print("----------------------------\n")

print(f"{Candit_Name[0]}: {Percent1:.3%} ({str(int(Candit1))})\n")

print(f"{Candit_Name[1]}: {Percent2:.3%} ({str(int(Candit2))})\n")

print(f"{Candit_Name[2]}: {Percent3:.3%} ({str(int(Candit3))})\n")

print("----------------------------\n")

print(f"Winner: {Winner}\n")

print("----------------------------\n")


# Print the Analysis in a text file
file_name = "PyPoll_Analysis.txt"
file_path = os.path.join('.','Analysis',file_name)

with open(file_path,"w") as f:
    f.write("Election Results\n\n")

    f.write("----------------------------\n\n")

    f.write("Total Votes: " + str(int(Num_votes)) + "\n\n")

    f.write("----------------------------\n\n")

    f.write(f"{Candit_Name[0]}: {Percent1:.3%} ({str(int(Candit1))})\n\n")

    f.write(f"{Candit_Name[1]}: {Percent2:.3%} ({str(int(Candit2))})\n\n")

    f.write(f"{Candit_Name[2]}: {Percent3:.3%} ({str(int(Candit3))})\n\n")

    f.write("----------------------------\n\n")

    f.write(f"Winner: {Winner}\n\n")

    f.write("----------------------------\n\n")

print("A seperate txt file named PyPoll_Analysis.txt has been created in Analysis folder")