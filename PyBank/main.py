import os
import csv


# Set path for file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")

    months = []
    revenue = []
    revenue_change = []
    revenue_average = []

    # read through each row of data after header
    for rows in csvreader:
        #track month
        months.append(rows[0])
        #track revenue
        revenue.append(int(rows[1]))
        
    total_months = len(months)
    
    # revenue change
    for x in range(1, len(revenue)):
        revenue_change.append((int(revenue[x]) - int(revenue[x-1])))
    
    # average revenue change
    revenue_average = sum(revenue_change) / len(revenue_change)
 

    # greatest increase in revenue
    greatest_increase = max(revenue_change)
    # greatest decrease in revenue
    greatest_decrease = min(revenue_change)


    # print the Results
    print("Financial Analysis")
    print(".----------------------------")
    print(f"total months: {total_months}")
    print(f"Total: $ {sum(revenue)}")
    print(f"Average change: ${round(revenue_average,2)}")
    print(f"Greatest Increase in Profits: {months[revenue_change.index(max(revenue_change))+1]} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {months[revenue_change.index(min(revenue_change))+1]} (${greatest_decrease})")


# write file
file = open("PyBank.txt","w")
file.write("Financial Analysis" + "\n")
file.write("----------------------------"+ "\n")
file.write(f"total months: {total_months}\n")
file.write(f"Total: $ {sum(revenue)}\n")
file.write(f"Average change: ${round(revenue_average,2)}\n")
file.write(f"Greatest Increase in Profits: {months[revenue_change.index(max(revenue_change))+1]} (${greatest_increase})\n")
file.write(f"Greatest Decrease in Profits: {months[revenue_change.index(min(revenue_change))+1]} (${greatest_decrease})")
file.close()




