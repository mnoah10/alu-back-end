#!/usr/bin/python3
"""Export all employees' TODO list data to a JSON file."""
import collections
import json
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    users = requests.get("{}/users".format(BASE_URL)).json()
    todos = requests.get("{}/todos".format(BASE_URL)).json()

    data = collections.OrderedDict()
    for user in users:
        user_id = user.get("id")
        tasks = []
        for task in todos:
            if task.get("userId") == user_id:
                item = collections.OrderedDict()
                item["username"] = user.get("username")
                item["task"] = task.get("title")
                item["completed"] = task.get("completed")
                tasks.append(item)
        data[str(user_id)] = tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)
