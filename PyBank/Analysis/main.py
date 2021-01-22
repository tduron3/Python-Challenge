import os
import csv

#List of Variables 
total_mths = 0
net_amt = 0
mth_chng = []
mth_ct = []
greatest_inc = 0
greatest_inc_mth = 0
greatest_decr = 0
greatest_decr_mth = 0

# Set File Path
csvpath = os.path.join('.', 'python-challenge', 'PyBank', 'Resources', 'budget_data.csv')


with open(csvpath, newline='') as csvfile:

#Clarify CSV Reader
   csvreader = csv.reader(csvfile, delimiter=',')

 #Clarify Header 
    csv_header = next(csvreader)

 #Clarify Row   
    csv_row = next(csvreader)

#Set DF
df = pd.read_csv(r'PyBank/Resources/budget_data.csv')

#Path for Output Text File
output_file = os.path.join('.', 'python-challenge', 'pybank', 'analysis', 'pybank.txt')

#Open File in Write Mode
with open(output_file,'w') as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {tot_mths}\n")
    txtfile.write(f"Total: ${net_amt}\n")
    txtfile.write(f"Average Change: ${avg_chg:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_incr_mth}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decr_mth}, (${lowest})\n")

    print (main.py)

    
