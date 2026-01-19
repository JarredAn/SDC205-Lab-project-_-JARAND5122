from datetime import datetime
import csv

# Function to convert temperature from Fahrenheit to Celsius
def convertData(temp_input):
    converted_value = (temp_input - 32) * 5.0/9.0
    return converted_value

# Function to get user input for temperature data and save to CSV file
def getInput():
    num_entries = int(input("How many entries are you entering? "))
    
    for i in range(num_entries):
        date_input = input("Enter the date: ")
        print()
        temp_input = float(input("Enter the temperature in fahrenheit: "))
        
        converted_value = convertData(temp_input)
        # Create comma-separated string
        data = f"{date_input},{temp_input},{converted_value}"
        
        # Save to CSV file
        try:
            insertData("ZooData.csv", data)
            current_time = datetime.now()
            print(f"The following data was saved at {current_time}: {data}")
            print()
        except Exception as e:
            print(f"Failed to save data: {e}")
            print()


# Function to insert data into a CSV file
def insertData(file_path, data):
    try:
        with open("C:\\PythonFiles\\zooData.csv", 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Split the comma-separated string and write as a row
            data_list = data.split(',')
            writer.writerow(data_list)
    except Exception as e:
        print(f"Error writing to file: {e}")
        raise

def viewData(file_path):
    try:
        print(f"Reading data from: {file_path}")
        print()
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        print(f"Error: The file 'zooData.csv' does not exist.")
    except Exception as e:
        print(f"Error reading file: {e}")


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
elif user_choice == '2':
    viewData("C:\\PythonFiles\\zooData.csv")
elif user_choice == '3':
    print("Error: The chosen functionality is not implemented yet.")
