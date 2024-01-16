"""A simple script to compare two JSON files."""

# Imports

import json
import os

def load_json(file_path: str) -> dict:
    """
    Load a JSON file and return the contents as a dictionary.
    :param file_path: The path to the JSON file to load.
    :return: The contents of the JSON file as a dictionary.
    """

    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Invalid JSON in file: {file_path}")
        return None

def compare_json(json1, json2, path: str = "") -> list:
    """
    Compare two JSON objects and return a list of differences.
    :param json1: The first JSON object to compare.
    :param json2: The second JSON object to compare.
    :param path: The path to the current JSON object.
    :return: A list of differences between the two JSON objects.
    """

    differences = []

    if json1 == json2:
        return differences

    if isinstance(json1, dict) and isinstance(json2, dict):
        for key in json1:
            if key not in json2:
                differences.append(f"Missing {path + key} in second JSON")
            else:
                differences.extend(compare_json(json1[key], json2[key], path + key + "."))

        for key in json2:
            if key not in json1:
                differences.append(f"Missing {path + key} in first JSON")

    elif isinstance(json1, list) and isinstance(json2, list):
        for i in range(max(len(json1), len(json2))):
            if i >= len(json1):
                differences.append(f"Missing {path}[{i}] in first JSON")
            elif i >= len(json2):
                differences.append(f"Missing {path}[{i}] in second JSON")
            else:
                differences.extend(compare_json(json1[i], json2[i], path + f"[{i}]."))

    else:
        differences.append(f"Different value at {path}: {json1} vs {json2}")

    return differences

def main() -> None:
    """
    The main function.
    :return: None
    """

    print(f"Note that the files have to be in the current working directory: {os.getcwd()}")

    json_file_1 = input("JSON file 1: ")
    json_file_2 = input("JSON file 2: ")

    json1 = load_json(json_file_1)
    json2 = load_json(json_file_2)

    if json1 is not None and json2 is not None:
        diffs = compare_json(json1, json2)
        if diffs:
            print("Differences found:")
            for diff in diffs:
                print(diff)
        else:
            print("No differences found.")

if __name__ == '__main__':
    main()