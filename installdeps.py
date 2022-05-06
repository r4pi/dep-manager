#!/usr/bin/env python3
"""
Custom system dependency installer for the the R4Pi project
"""
import json
import subprocess
import sys

try:
    with open("project-deps.json", "r") as stream:
        try:
            deps_list = json.load(stream)
        except:
            print("Error: File not found")
            sys.exit(1)
except Exception as err:
    print("File not found")
    sys.exit(1)


try:
    cmd = sys.argv[1]
except IndexError as err:
    print("Available commands:")
    for key in deps_list.keys():
        print("* {} - {}".format(key, deps_list[key]["description"]))
    sys.exit(1)

print(deps_list[cmd]["pkgs"])


process = subprocess.run(
    ["sudo", "apt", "update"],
    stdout=subprocess.PIPE,
    universal_newlines=True,
    check=False,
)
print(process)

command = ["sudo", "apt", "install", "-y"]

command.extend(deps_list[cmd]["pkgs"])

process = subprocess.run(
    command, stdout=subprocess.PIPE, universal_newlines=True, check=False
)
print(process)
