#Psuedo Code Plan
#Sum of votes cast
#Loop to find unique candidates
#Variable for votes for each candidate
#Divide votes for each by candidate by total votes
# Who go thte most votes 

#Importing CSV data

import os
import csv

csvpath = os.path.join(os.path.abspath(__file__),'..','Resources','election_data.csv')

#Total Votes

TotalVotes = 0
TotalCandidates = []
Candidates = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        TotalVotes += 1
        TotalCandidates.append(row[2])
        Candidates[row[2]] = Candidates.setdefault(row[2],0) + 1
print(csv_header)
print(TotalVotes)

#Unique Candidate List

UniqueCandidates = set(TotalCandidates)

#Percent of Vote per Candidate

KhanVotedec = round(int(Candidates["Khan"])/TotalVotes, 3)
CorreyVotedec = round(int(Candidates["Correy"])/TotalVotes, 3)
LiVotedec = round(int(Candidates["Li"])/TotalVotes, 3)
OTooleyVotedec = round(int(Candidates["O'Tooley"])/TotalVotes, 3)

KhanVotePercent = "{:.0%}".format(KhanVotedec)
CorreyVotePercent = "{:.0%}".format(CorreyVotedec)
LiVotePercent = "{:.0%}".format(LiVotedec)
OTooleyVotePercent = "{:.0%}".format(OTooleyVotedec)

#Total Votes per Candidate

KhanVote = round(int(Candidates["Khan"]), 3)
CorreyVote = round(int(Candidates["Correy"]), 3)
LiVote = round(int(Candidates["Li"]), 3)
OTooleyVote = round(int(Candidates["O'Tooley"]), 3)

#OutPut

print(UniqueCandidates)

print(KhanVotePercent)
print(CorreyVotePercent)
print(LiVotePercent)
print(OTooleyVotePercent)

print(KhanVote)
print(CorreyVote)
print(LiVote)
print(OTooleyVote)