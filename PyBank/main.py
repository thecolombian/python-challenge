import csv

# Import the CSV module to handle the file type

from datetime import datetime

#Import datetime module to timestamp when the report was generated - I added it as a way to know when I ran the script
# it fails if you run it inside the Visual Code as the path fails - if you run it manually it works just fine

# Define the file path to the CSV file
file_path = '../Resources/budget_data.csv'

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = None
# declaring lists with NO values - just in case :) 
changes = []
months = []

# Read the CSV file
with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        # Extract date and profit/loss
        date = row['Date']
        profit_loss = int(row['Profit/Losses'])

        # Calculate the total number of months and net total amount of "Profit/Losses"
        total_months += 1
        net_total += profit_loss

        # Calculate changes in "Profit/Losses"
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            months.append(date)

        # Set the previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(changes) / len(changes)

# Determine the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_increase_date = months[changes.index(greatest_increase)]
greatest_decrease_date = months[changes.index(greatest_decrease)]

# Get the current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Generate the financial analysis results
results = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
    f"\n\n\nReport generated on: {current_datetime}\n"
)

# Print the analysis to the terminal
print(results)

# Export the results to a text file
#It will override the contents of the current file
with open('../analysis/financial_analysis.txt', mode='w') as output_file:
    output_file.write(results)
