import os
import csv

# Path to collect data from the Resources folder
budgetdata_csv = os.path.join('..', 'Resources', 'budget_data.csv')

def as_currency(amount):
   return '$:,.2f'.format(amount)

# Read in the CSV file
with open(budgetdata_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header
    header = next(csvreader)

  
    profitorloss = 0
    rowcount = 0
    greatestincrease = 0
    great_inc_date = 'Jan-9999'
    greatestdecrease = 0
    great_dec_date = 'Jan-9999'
    #rowcount = sum(1 for row in csvreader)

    #Loop through the data
    for row in csvreader:
        profitorloss += int(row[1])
        rowcount += 1
        if greatestincrease <= int(row[1]):
           greatestincrease = int(row[1])
           great_inc_date = str(row[0])
        if greatestdecrease >= int(row[1]):
           greatestdecrease = int(row[1])
           great_dec_date = str(row[0])


        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
     #   if name_to_check == row[0]:
      #      print_percentages(row)

print("Financial Analysis")
print("--------------------------------------")
print(f"Total Months:  {rowcount} ")
print(f'Total: ${profitorloss:.0f}'.replace('$-', '-$'))
print(f'Average Change: ${profitorloss / rowcount :.2f}'.replace('$-', '-$'))
print(f'Greatest Increase in Profits: {great_inc_date}, $({greatestincrease:.0f})'.replace('$-', '-$'))
print(f'Greatest Decrease in Profits: {great_dec_date}, $({greatestdecrease:.0f})'.replace('$-', '-$'))



#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)
