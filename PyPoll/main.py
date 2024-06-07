import csv

# Import the CSV module to handle the file type

from datetime import datetime

# Define the file path to the CSV file
file_path = '../Resources/election_data.csv'

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Read the CSV file
with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        # Extract candidate name
        candidate = row['Candidate']

        # Increment total votes
        total_votes += 1

        # Tally votes for each candidate
        # next time I need to use better labels :)
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Get the current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Calculate the percentage of votes for each candidate and determine the winner
results = (
    "Election Results\n"
    "\n-------------------------\n\n"
    f"Total Votes: {total_votes}\n"
    "\n-------------------------\n\n"
)
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results += f"{candidate}: {percentage:.3f}% ({votes})\n\n"
    if votes > max_votes:
        max_votes = votes
        winner = candidate
results += (
    "\n-------------------------\n\n"
    f"Winner: {winner}\n"
    "\n-------------------------\n"

    f"\n\n\nReport generated on: {current_datetime}\n"
)

# Print the analysis to the terminal
print(results)

# Export the results to a text file
with open('../analysis/election_results.txt', mode='w') as output_file:
    output_file.write(results)
