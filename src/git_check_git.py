import requests

import os

 

# Configuration

GITHUB_RAW_URLS = [

    "https://raw.githubusercontent.com/syljan/repository/bobik_ev3_2025/blob/master/Hello_Bobik.py",


]

LOCAL_DIR = "./downloaded_scripts"

 

# Create local directory if not exists

os.makedirs(LOCAL_DIR, exist_ok=True)

 

# Download and execute each script

for url in GITHUB_RAW_URLS:

    filename = url.split("/")[-1]

    local_path = os.path.join(LOCAL_DIR, filename)

 

    # Download file

    response = requests.get(url)

    if response.status_code == 200:

        with open(local_path, "w", encoding="utf-8") as f:

            f.write(response.text)

        print(f"Downloaded: {filename}")

 

        # Execute the script safely

        print(f"Executing: {filename}")

        with open(local_path, "r", encoding="utf-8") as f:

            code = f.read()

            exec(code, {})  # Executes in an isolated dictionary

   