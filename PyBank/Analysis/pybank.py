import os
import csv

#absolute path to access .csv file 
pybank_csv = os.path.join(r"C:\Users\jwhit\Desktop\github\python-challenge\PyBank\Resources\budget_data.csv")

#initial list for column values
dates = []
balances = []

#read .csv file
with open (pybank_csv, mode = 'r') as csvfile:
    #set delimiter to comma
    csv_reader = csv.reader(csvfile, delimiter=",")
    #store header row
    csv_header = next(csv_reader)
    #define where the values for the lists are located
    for row in csv_reader:
        dates.append(row[0])
        balances.append(int(row[1]))

#define function with two parameters: dates and balances
def summary(dates, balances):
    total_months = len(dates)
    net_profit = sum(balances)
    if total_months > 1:
        profit_changes = [balances[i] - balances[i-1] for i in range (1, len(balances))]
        average_change = sum(profit_changes) / len(profit_changes)
        highest_profit = max(profit_changes)
        highest_loss = min(profit_changes)
        highest_profit_date = dates[profit_changes.index(highest_profit) + 1]
        highest_loss_date = dates[profit_changes.index(highest_loss) + 1]
    else:
        profit_changes = [0]
        average_change = 0
        highest_profit = 0
        highest_profit_date = "N/A"
        highest_loss_date = "N/A"


    #define the summary box in order to export and print easier
    summary_box = (
    "Financial Analysis\n"
    "--------------------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_profit}\n"
    f"Average Change: ${average_change: .2f}\n"
    f"Greatest Increase in Profits: {highest_profit_date} (${highest_profit})\n"
    f"Greatest Decrease in Profits: {highest_loss_date} (${highest_loss})"
    )


    #print summary box
    print(summary_box)

    #create new text file containing summary box
    output_file = "pybank.txt"
    with open(output_file, "w") as file:
        file.write(summary_box)

#run summary function
summary(dates, balances)