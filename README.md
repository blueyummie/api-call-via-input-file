# Make API calls from an input .yaml file
This program will prompt user for an input .yaml file path.  It will then automatically make API requets to every URL in the yaml every 15 seconds until user stops the program with a keyboard inturruption. While it's making these API calls, it will calcualte the UP time for each domain and print it to console.

# Prerequisites
Ensure you have the following installed:
- Python (version 3.X)
- Required dependencies (listed in requirements.txt)
- Virtual enviornment (optional but reccomended)

# Installation
1. Clone the repository:
   
   ```git clone https://github.com/blueyummie/api-call-via-input-file.git```
2. Navigate to your project directory:

   ```cd projectdirectory```

3. Create a virtual environment (optional but recommended):

   ```python -m venv venv source```
   
   ```source venv/bin/activate```
4. Install required modules:

   ```pip install -r requirements.txt```

# Usage
Run main.py. You will be prompted to input a file path. Put in the exact file path
