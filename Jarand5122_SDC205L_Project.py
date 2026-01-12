from datetime import datetime

# Function to convert temperature from Fahrenheit to Celsius
def convertData(temp_input):
    converted_value = (temp_input - 32) * 5.0/9.0
    return converted_value

# Function: getInput prompts user for entries  and prints results
def getInput():
    num_entries = int(input("How many entries are you entering? "))
    
    for i in range(num_entries):
        date_input = input("Enter the date: ")
        print()
        temp_input= float(input("Enter the temperature in farenheit): "))
        
        converted_value = convertData(temp_input)
        
        print(f"The following was saved at {datetime.now()} : ")
        print(f"{date_input}, {temp_input}, {converted_value}")

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
    
if user_choice == '1':
    getInput()
else:
    print("Error: The chosen functionality is not implemented yet.")