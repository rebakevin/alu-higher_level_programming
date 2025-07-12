#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a JSON file.
Uses save_to_json_file and load_from_json_file functions.
"""

import sys
from os.path import exists

def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    import json
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

if __name__ == "__main__":
    filename = "add_item.json"
    
    # Load existing list from file if it exists, otherwise create empty list
    if exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []
    
    # Add all command line arguments to the list
    my_list.extend(sys.argv[1:])
    
    # Save the updated list to the JSON file
    save_to_json_file(my_list, filename)
