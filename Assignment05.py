# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Phuong Tran>,<11/16/2024>, <Assignment05>
# ------------------------------------------------------------------------------------------ #
from logging import raiseExceptions

import json  # Import the JSON module for reading and writing JSON data.

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"  # Constant for the JSON file name.

# Define the Data Variables and constants
student_first_name: str = ''        # Holds the first name of a student entered by the user.
student_last_name: str = ''         # Holds the last name of a student entered by the user.
course_name: str = ''               # Holds the name of a course entered by the user.
student_data: dict[str, str] = {}   # Dictionary to hold one row of student data.
students: list = []                 # List of dictionaries, representing a table of student data.
menu_choice: str                    # Holds the user's menu choice.

# When the program starts, read the file data into the list of dictionaries.
try:
    file = open(FILE_NAME, "r")       # Open the JSON file in read mode.
    json_data = file.read()           # Read the entire file content as a string.
    students = json.loads(json_data)  # Parse the JSON string into a list of dictionaries.
except FileNotFoundError:
    print('File not found. Creating a new file...')  # If file does not exist, print a message.
    open(FILE_NAME, 'w').close()                     # Create an empty file if it does not exist.
    students = []                                    # Initialize the students list as empty.
except json.JSONDecodeError:
    print('JSON decoding error. Resetting the data...')  # If JSON is invalid, reset the data.
    students = []                                        # Initialize the students list as empty.
except Exception as e:
    print('Unknown exception. Resetting roster...')      # Catch any other exception.
    students = []                                        # Initialize the students list as empty.
    print(type(e), e)                                    # Print the exception type and message.
finally:
    if file and not file.closed:  # Ensure the file is closed if it was opened.
        file.close()              # Close the file.

# Main program loop
while True:
    print(MENU)                                         # Display the menu to the user.
    menu_choice = input("What would you like to do: ")  # Get the user's menu choice.

    # Option 1: Register a student
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ").strip()  # Get the student's first name.
            if not student_first_name.isalpha():                                    # Check if the name is alphabetic.
                raise ValueError('First name must be alphabetic')                   # Raise an error if invalid.

            student_last_name = input("Enter the student's last name: ").strip()    # Get the student's last name.
            if not student_last_name.isalpha():                                     # Check if the name is alphabetic.
                raise ValueError('Last name must be alphabetic')                    # Raise an error if invalid.

            course_name = input("Please enter the name of the course: ").strip()    # Get the course name.
            student_data = {
                "FirstName": student_first_name,
                "LastName": student_last_name,
                "CourseName": course_name
            }  # Create a dictionary for the student's data.
            students.append(student_data)  # Add the student's data to the list.
            print(f"Registered {student_first_name} {student_last_name} for {course_name}.")  # Confirmation message.
        except ValueError as e:
            print(e)  # Print the error message.

    # Option 2: Display current data
    elif menu_choice == "2":
        print("-" * 50)               # Print a separator line.
        if students:                  # Check if there are any students registered.
            for student in students:  # Loop through each student dictionary.
                try:
                    print(
                        f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
                except KeyError as e:
                    print(f"Missing data: {e}")             # Handle missing keys in the dictionary.
        else:
            print("No students are currently registered.")  # Inform the user if the list is empty.
        print("-" * 50)                                     # Print a closing separator line.

    # Option 3: Save the data to a JSON file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")                 # Open the JSON file in write mode.
            json_data = json.dumps(students, indent=4)  # Convert the list of dictionaries to a JSON string.
            file.write(json_data)                       # Write the JSON string to the file.
            print("Data successfully saved to file.")   # Confirmation message.
        except Exception as e:
            print('Error saving data to file:', e)      # Print an error message if saving fails.
        finally:
            if file and not file.closed:                # Ensure the file is closed.
                file.close()                            # Close the file.

    # Option 4: Exit the program
    elif menu_choice == "4":
        print("Exiting the program")                    # Exit message.
        break                                           # Exit the loop and end the program.

    # Invalid menu choice
    else:
        print("Please only choose option 1, 2, 3, or 4") # Inform the user of an invalid choice.

print("Program Ended")                                   # Final message when the program ends.
