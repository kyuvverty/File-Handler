# Importing libraries
import os
from format_data import *

# ------------------------------------------------- -------------------------------------------------- --------

# Total number of files (will be filled in automatically)
files_count = 0

# Number of problem files (will be filled in automatically)
bad_count = 0

# Number of successfully processed files (will be filled in automatically)
good_count = 0

# List of files in the input folder (will be filled in automatically)
input_files = []

# List of successfully processed files (will be filled in automatically)
good_files = []

# List of problem files (will be filled in automatically)
bad_files = []

#-------------------------------------------------- -------------------------------------------------- -------

# Check format_list for errors
"".format_map(format_list)

# Iterate through the files in the input folder and add them to the input_files list
for file in os.listdir("INPUT"):
    input_files.append(file)
    files_count += 1
# Iterate through all files from the input_files list and perform the appropriate actions
for file_name in input_files:

    # Open a file
    file = open(f"INPUT/{file_name}", 'r', encoding="utf-8")
    try:
        # Read and format the contents of the file, storing it in the formated_text variable
        formated_text = file.read().format_map(format_list)

        # Write the contents of the formated_text variable to a file with the same file name in the output folder
        with open(f"OUTPUT/{file_name}", 'w', encoding="utf-8") as file:
            file.write(formated_text)

    # If a KeyError exception is thrown during processing
    except KeyError:
        print(f"\nE: A KeyError exception occurred while reading or writing file {file_name}!")
        bad_files.append(file_name)
        bad_count += 1

    except ValueError:
        print(f"\nE: A ValueError exception occurred while reading or writing file {file_name}!")
        bad_files.append(file_name)
        bad_count += 1
# If the file is processed successfully
    else:
        print(f"\nFile {file_name} processed successfully!")
        good_files.append(file_name)
        good_count += 1
        
    # Closing the file, regardless of success of processing
    finally:
        file.close()

#-----------------------------------------------------------------------------------------------------------

# End, select next actions"
print("\n\n\n----------------------------------")
print(f"Total files: {files_count}")
print(f"Processed: {good_count}")
print(f"Problem files: {bad_count}")
print("----------------------------------")
print("1. Close the program")
print("2. Delete successfully processed files from the 'input' folder and close the program")
print("3. Remove problematic files from the 'input' folder and close the program")
print("4. Delete all files from the 'input' folder and close the program\n")

input_process = 1
while input_process == 1:
    # Input
    answer = str(input('>'))

    # If the answer is 1
    if answer == "1":
        input_process = 0

    # If the answer is 2, delete the processed files in the 'input' folder
    elif answer == "2":
        for file in good_files:
            os.remove(f"INPUT/{file}")
        input_process = 0
    
    # If the answer is 3, delete the problematic files in the 'input' folder
    elif answer == "3":
        for file in bad_files:
            os.remove(f"INPUT/{file}")
        input_process = 0
    
    # If the answer is 4, delete all files in the 'input' folder
    elif answer == "4":
        for file in input_files:
            os.remove(f"INPUT/{file}")
        input_process = 0