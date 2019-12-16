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


# Specify the file to write to
output_path = os.path.join("..", "Resources", "output_for_budgetdata.txt")
# Should have defined these earlier than print o h well
String_1 = "Total Months: " + str(rowcount) + "\n"
String_2 = "Total : $" + str((profitorloss)) + "\n"
String_3 = f'Average Change: ${profitorloss / rowcount :.2f}'.replace('$-', '-$') + "\n"
String_4 = f'Greatest Increase in Profits: {great_inc_date}, $({greatestincrease:.0f})'.replace('$-', '-$') + "\n"
String_5 = f'Greatest Decrease in Profits: {great_dec_date}, $({greatestdecrease:.0f})'.replace('$-', '-$') + "\n"

# Open the file using "write" mode. Specify the variable to hold the contents

with open(output_path, 'w', newline='') as file:

    # Write the first row (column headers)
    file.write("Financial Analysis\n")
 
    # Write the second row
    file.write("----------------------------------------------\n")


    # Write the Third row
    file.write(String_1)

        # Write the fourth row
    file.write(String_2)

       # Write the fifth row
    file.write(String_3)

        # Write the sixth row
    file.write(String_4)

            # Write the seventh row
    file.write(String_5)