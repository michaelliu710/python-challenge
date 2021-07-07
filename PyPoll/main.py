import os
import csv
import pandas as pd

# Set path for file
data_file = pd.read_csv("Resources/election_data.csv")
#print(data_file)


# The total number of votes cast
votes = len(data_file)
votes

# A complete list of candidates who received votes
candidateCount = data_file["Candidate"].value_counts()
candidateCount


# percentage of votes each candidate won
percent_votes = (candidateCount/votes)*100
percent_votes


# announce the winner
winner = candidateCount.idxmax()
winner


# print the results
print("Election results")
print("--------------------------------------------------------------------------")
print("Total votes: " + str(votes))
print("----------------------------------------------------------------------------")
print("Khan:" + " " + str(round(percent_votes[0],3)) + "%" + "("+str(candidateCount[0])+")")   
print("Correy:" + " " + str(round(percent_votes[1],3)) + "%" + "("+str(candidateCount[1])+")")     
print("Li:" + " " + str(round(percent_votes[2],3)) + "%" + "("+str(candidateCount[2])+")")     
print("O'Tooley:" + " " + str(round(percent_votes[3],3)) + "%" + "("+str(candidateCount[3])+")")
print("----------------------------------------------------------------------------------------")     
print("winner: " + winner)



# convert the output into a text file
file = open('pypoll.txt','w')
file.write("Election results")
file.write("\n-------------------------")
file.write("\nTotal votes: " + str(votes))
file.write("\n-------------------------")
file.write("\nKhan:" + " " + str(round(percent_votes[0],3)) + "% " + "("+str(candidateCount[0])+")")
file.write("\nCorrey:" + " " + str(round(percent_votes[1],3)) + "% " + "("+str(candidateCount[1])+")")
file.write("\nLi:" + " " + str(round(percent_votes[2],3)) + "% " + "("+str(candidateCount[2])+")")
file.write("\nO'Tooley:" + " " + str(round(percent_votes[3],3)) + "% " + "("+str(candidateCount[3])+")")
file.write("\n-------------------------")
file.write("\nwinner: " + winner)
file.close()


