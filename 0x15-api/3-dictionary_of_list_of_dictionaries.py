#!/usr/bin/python3
"""A REST API implementation to fetch employee info"""
import json
import requests
import sys

if __name__ == "__main__":
	url = "https://jsonplaceholder.typicode.com/"

	user = requests.get(url + "users").json()

	data_to_export = {}

	for user in user:
		user_id = user["id"]

		todos_response = requests.get(url + f"todos?userid={user_id}")

		todo_list = todos_response.json()

		data_to_export[user_id] = []

	for todo in todo_list:
		task_info = {
				"username" : user.get("username"),
				"task": todo.get("title"),
				"completed" : todo.get("completed")
		}
		data_to_export[user_id].append(task_info)

	with open("todo_all_employees.json", "w") as jsonfile:
		json.dump(data_to_export, jsonfile, indent=5)



	

