import os
import csv

#absolute path to .csv file
pypoll_csv = os.path.join(r"C:\Users\jwhit\Desktop\github\python-challenge\PyPoll\Resources\election_data.csv")

#initial dictionary setup
candidates = {}

#read csv file as a Dictionary
with open(pypoll_csv, newline= "") as csvfile:
    csv_reader = csv.DictReader(csvfile)
    #returns the unique candidates who received votes
    for row in csv_reader:
        candidate = row["Candidate"]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

#calculate total votes for all candidates
total_votes = sum(candidates.values())
#return votes per candidate, and divides by total votes 
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}
#finds the winner based on who received the most votes
winner = max(candidates, key=candidates.get)

#create a summary box to print and export easier
summary_box = [

"Election Results\n"
"---------------------------\n"
f"Total Votes: {total_votes}\n"
"---------------------------\n"
]

#returns values unique to each candidate and adds them to the summary box
for candidate, votes in candidates.items():
    percentage = candidate_percentages[candidate]
    summary_box.append(f"{candidate}: {percentage: .2f}% ({votes})\n")
summary_box.append("---------------------------\n")
summary_box.append(f"Winner: {winner}\n")
summary_box.append("---------------------------\n")


#print summary box
for line in summary_box:
    print(line, end="")

#create .txt file named 'pypoll'
output_file = "pypoll.txt"

with open(output_file, "w") as file:
    file.writelines(summary_box)
