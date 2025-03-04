import time
import yaml
import requests

# Variables
domain_total_dict = {}

# Get input from user
file_path = input("Please enter the full path with extension of the yaml file: ")

# Method for making the API requests
def make_request(url: str, request_method: str = "GET", headers: dict = None,  body: dict = None):

    # If a body is not passed in, then use method that doesn't require a body
    if body is not None:
        response = requests.request(method=request_method, url=url, headers=headers, json=body)

    else:
        response = requests.request(method=request_method, url=url, headers=headers)

    # Calculate response time and domain
    response_time = round(response.elapsed.total_seconds() * 1000, 1)
    domain = api['url'].split('/')

    # If domain doesn't exist, add it to the dictionary
    if domain[2] not in domain_total_dict:
        domain_total_dict[domain[2]] = {
            "attempts": 0,
            "successes": 0
        }

    # Add attempt counter for total calls, and if it's a success, add to dictionary
    domain_total_dict[domain[2]]["attempts"] += 1
    if 200 <= response.status_code < 300 and response_time <= 500:
        domain_total_dict[domain[2]]["successes"] += 1
        status = 'succesfull'
    else:
        status = 'down'
    success = domain_total_dict[domain[2]]["successes"]
    total = domain_total_dict[domain[2]]["attempts"]
    uptime_percentage = int(success/total*100) if total > 0 else 0
    print(f"{domain[2]} has {uptime_percentage}% availability percentage.")

# Load in yaml
with open(file_path, "r") as file:
    fetch_yaml = yaml.safe_load(file)

# Endless loop to call every domain every 15 seconds, until interrupted by user
try:
    while True:
        for api in fetch_yaml:
            request_method = api.get("method", "GET")
            make_request(api["url"], request_method=request_method)
        time.sleep(15)
except KeyboardInterrupt:
    print("Stopped by user.")
