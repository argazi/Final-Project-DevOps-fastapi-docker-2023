from fastapi import FastAPI
import requests

app = FastAPI()

JAVA_SERVER_URL = "http://10.100.102.41:8080/logs"

test_log_data = {
    "date": "2022-02-12T12:00:00",
    "route": "/hello"
}

def assert_and_print(expected, actual, field_name):
    if expected == actual:
        print(f"{field_name} - PASSED")
    else:
        print(f"{field_name} - FAILED")

def is_server_up(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

@app.get("/run-tests")
def run_tests():
    if not is_server_up(JAVA_SERVER_URL):
        return "Java server is not running or is not accessible."

    response = requests.post(JAVA_SERVER_URL, json=test_log_data)
    response_data = response.json()

    assert_and_print("/hello", response_data["route"], "Route Check")
    assert_and_print("2022-02-12T12:00:00", response_data["date"], "Date Check")
    assert_and_print(int, type(response_data["id"]), "ID Type Check")

    logs_response = requests.get(JAVA_SERVER_URL)
    logs = logs_response.json()

    if response_data in logs:
        print("Log Insertion - PASSED")
        return "Java server passed all tests"
    else:
        print("Log Insertion - FAILED")
