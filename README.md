# Make API calls from an input .yaml file
- This program will prompt user for an input .yaml file.  It will then automatically make API requets to every unique URL in the yaml every 15 seconds until user stops the program with a keyboard inturruption. While it's making these API calls, it will calculate the UP time for each domain and print it to console.
- "UP" is defined as any call that has <= 500ms response time AND returns a 200-299 http response code.

# Prerequisites
Ensure you have the following installed:
- Python (version 3.X)
- Git installed
- Required dependencies (listed in requirements.txt)
- Virtual enviornment (optional but reccomended)
- Valid .yaml file

# Installation
1. Clone the repository:
   
   ```git clone https://github.com/blueyummie/api-call-via-input-file.git```
2. Navigate to your project directory:

   ```cd c:\your\Cloned\Directory\```

3. Create a virtual environment (optional but recommended):

   ```python -m venv venv source```
   
4. Install required modules:

   ```pip install -r requirements.txt```

# Usage
- Run main.py.
   - If on Windows:

      ```python ./main.py```

   - If on Mac:

      ```python3 ./main.py```

- You will be prompted to input a file path. Enter the full file path. For this particular example, use this to make it work with the example in this repo:

   ```./input_yaml_directory/input.yaml```
