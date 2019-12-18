import os
import csv
import pandas as pd

# Path to collect data from the Resources folder
#electiondata_csv = os.path.join('..', 'Resources', 'election_data.csv')

#print(electiondata_csv)

#data_df = pd.read_csv('C:\\Desktop\\python-challenge\\Resources\\election_data.csv', encoding='iso-8859-1')
data_df = pd.read_csv(r'/Users/ashwinpatel/Desktop/python-challenge/Resources/election_data.csv')
# Read in the CSV file
TV = len(data_df.index)


g1 = data_df.groupby('Candidate').count()

# drop county col and rename votre id to total counts
g2 = g1.drop(['County'], axis=1)
g3 = g2.rename(columns={"Voter ID": "Total Counts"})

#print(f"a  : {g3}")

# drop county col and rename voter id to total percentage - sum by candidate also
f1 = g1.apply(lambda x: 100*x/TV)
f2 = f1.drop(['County'], axis=1)
f3 = f2.rename(columns={"Voter ID": "Total Percentage"})

#get maximum value to pick winner
idmax_val = f3.idxmax(axis=0)


#print(f"b  : {f4}")
#print(f"b  : {f3}")

#Merge both dataframes
print("Election Results")
print("-------------------------------------------")
print(f"Total Votes : {TV} " )
print("-------------------------------------------")

result = pd.concat([f3.round(3), g3], axis=1, sort=False)
result_sorted = result.sort_values(by='Total Percentage',  ascending=False)
print(f"D  : {result_sorted}")
print("-------------------------------------------")
print(f" Winner: {idmax_val} ")
print("-------------------------------------------")



#print(f"D  : {result}")