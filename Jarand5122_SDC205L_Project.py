from datetime import datetime

print ("Jarand5122's Excel Spreadsheet Automation Menu")
print ("Choose a number from the following options:")
print ("1. Input Data")
print ("2. View Current Data")
print ("3. Generate Report")

user_choice = input()
if user_choice not in ['1', '2', '3']:
    print ("Invalid option selected. Please choose 1, 2, or 3.")
else:
    print (f"You selected option {user_choice} at {datetime.now()}")