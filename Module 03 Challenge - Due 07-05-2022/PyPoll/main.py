
import os
import csv

election_csv = os.path.join( "Resources", "election_data.csv")
outputFile = os.path.join("Resources", "election_data_output.txt")

totalVotes = 0
candidatesNames = []
candidatesVotes = {}
candidatesNamesAndVotes = []
votes = []
candidatesWinner = []

with open(election_csv) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvfile)
    
    for row in csv_reader:
        totalVotes += 1
    
        if row[2] not in candidatesNames:
            candidatesNames.append(row[2])
            
            candidatesVotes[row[2]] = 1
        else:
            candidatesVotes[row[2]] += 1

for candidate in candidatesVotes:
    vote = candidatesVotes.get(candidate)
    votes.append(vote)
    votePc = (float(vote) * 100)/ float(totalVotes)
    candidateOutput = f"{candidate}: {votePc:.3f}% ({vote})"
    candidatesNamesAndVotes.append(candidateOutput)

candidatesWinner = [candidatesNames[0], votes[0]]


for i in range(len(votes)):
    if (votes[i] > candidatesWinner[1]):
        candidatesWinner[1] = votes[i]
        candidatesWinner[0] = candidatesNames[i]

output = (
    f"Election Results \n"
    f"---------------------------\n"
    f"Total Votes: {totalVotes}\n"
    f"---------------------------\n"
    f"{candidatesNamesAndVotes[0]}\n"
    f"{candidatesNamesAndVotes[1]}\n"
    f"{candidatesNamesAndVotes[2]}\n"
    f"---------------------------\n"
    f"Winner: {candidatesWinner[0]}\n"
    f"---------------------------"
)

print(output)

with open(outputFile, "w") as textfile:
    textfile.write(output)