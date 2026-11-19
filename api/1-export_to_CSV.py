#!/usr/bin/python3
"""Export an employee's TODO list data to a CSV file."""
import csv
import requests
import sys


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

    with open("{}.csv".format(employee_id), "w", newline="") as csv_file:
        writer = csv.writer(
            csv_file, quoting=csv.QUOTE_ALL, lineterminator="\n"
        )
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title"),
            ])
