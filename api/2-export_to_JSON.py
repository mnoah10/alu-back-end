#!/usr/bin/python3
"""Export an employee's TODO list data to a JSON file."""
import json
import requests
import sys
from collections import OrderedDict


BASE_URL = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    user = requests.get("{}/users/{}".format(BASE_URL, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(BASE_URL), params={"userId": employee_id}
    ).json()

    username = user.get("username")

    tasks = []
    for task in todos:
        item = OrderedDict()
        item["task"] = task.get("title")
        item["completed"] = task.get("completed")
        item["username"] = username
        tasks.append(item)

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump({str(employee_id): tasks}, json_file)
