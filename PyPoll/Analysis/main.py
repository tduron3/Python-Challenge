import os
import csv

# Set File Path
csvpath = os.path.join('.', 'python-challenge', 'PyPoll', 'Resources', 'election_data.csv')

# Define function to use 'Election_data' as sole parameter
def percent_votes_candidate(election_data):

#List of Variables 
    Voter_ID = int(election_data[0]
    County = str(election_data[1])
    Candidates = str(election_data[2])
    total_votes_cast = 0
    list_candidates = []
    All_Candidates = []
    percent_votes_candidate = {}
    mth_ct = []
    total_nbr_votes_candidate = 0
    election_winner_pop = ""

# Read in the CSV File
with open(csvpath, newline='') as csvfile:

# Clarify CSV Reader
   csvreader = csv.reader(csvfile, delimiter=',')
   csv_row=next(csvreader)

 # Clarify Row   
    for row in csvreader:
        total_votes_cast = Total_votes_cast +1
        candidates = row[2]
        voter_ID=row[0]
        county=row[1]
        voter_IDs.append(voter_ID)
        counties.append(county)
        candidates.append(candidate)
        if candidate in total_nbr_votes_candidate:
            total_nbr_votes_candidate[Candidates] = total_nbr_votes_candidate[Candidates] +1
            else:
            total_nbr_votes_candidate[candidate] = 1





# Path for Output Text File
output_file = os.path.join('.', 'python-challenge', 'pybank', 'analysis', 'pybank.txt')

# Open File in Write Mode
with open(output_file,'w') as txtfile:
    txtfile.write(f"Total_Votes_Cast\n")
    txtfile.write(f"list_candidates\n")
    txtfile.write(f"Percent_Votes_Candidate\n")
    txtfile.write(f"Mth_Count\n")
    txtfile.write(f"Total_Nbr_of_Votes_Candidate\n")
    txtfile.write(f'Election_Winner_Pop')
   

print(f"Total_Votes_Cast")
print(f"list_candidates")
print(f"Percent_Votes_Candidate")
print(f"Mth_Count")
print (f"Total_Nbr_of_Votes_Candidate")
