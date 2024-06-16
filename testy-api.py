import os
import json
import subprocess

def send_request(url):
    result = subprocess.run(['curl', '-s', url], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def check_response(response, keys):
    try:
        response_json = json.loads(response)
    except json.JSONDecodeError:
        return False, "Invalid JSON"
    
    for key in keys:
        if key not in response_json:
            return False, f"Missing key: {key}"
    return True, ""

def test_endpoint(url, keys):
    response = send_request(url)
    if response:
        passed, message = check_response(response, keys)
        if passed:
            print(f"Test for {url}: PASSED")
        else:
            print(f"Test for {url}: FAILED ({message})")
    else:
        print(f"Test for {url}: FAILED (No response)")

if __name__ == "__main__":
    endpoints = [
        {"url": "https://jsonplaceholder.typicode.com/posts/1", "keys": ["userId", "id", "title", "body"]},
        {"url": "https://jsonplaceholder.typicode.com/users/1", "keys": ["id", "name", "username", "email"]},
        {"url": "https://jsonplaceholder.typicode.com/todos/1", "keys": ["userId", "id", "title", "completed"]}
    ]
    
    for endpoint in endpoints:
        test_endpoint(endpoint["url"], endpoint["keys"])
