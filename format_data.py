# Importing libraries
import os
import time

# Dictionary with data to format (format_map)
# Add your own keys with values ​​to the dictionary
format_list = {
    
    # Output date and time
    "full_date": time.ctime(),

    # PC username
    "user": os.getlogin(),

    # Message in curly braces
    'test': '{hello_world}'
    }