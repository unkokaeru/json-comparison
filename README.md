# JSON Comparison Script

## Overview

This script provides a simple and efficient way to compare two JSON files. It identifies and reports differences between them, making it particularly useful for tasks like data verification, debugging, and ensuring consistency across files.

## Features

- **Load JSON Files**: Reads JSON files and converts their contents into Python dictionaries.
- **Comparison**: Compares two JSON objects, either dictionaries or lists, and identifies differences.
- **Error Handling**: Includes basic error handling for missing files and invalid JSON formats.
- **User Input**: Allows users to specify the paths of the JSON files they want to compare.
- **Detailed Reporting**: Outputs a list of differences found between the two JSON files.

## Requirements

- Python 3.x
- Standard Python libraries: `json`, `os`

## Installation

No additional installation is required. Ensure Python 3.x is installed on your system.

## Usage

1. Place the script in the directory containing the JSON files to be compared.
2. Run the script using Python: `python json-comparison.py`
3. When prompted, enter the names of the two JSON files you wish to compare.

## Function Descriptions

- `load_json(file_path: str) -> dict`: Loads a JSON file and returns its contents as a dictionary.
- `compare_json(json1, json2, path: str = "") -> list`: Compares two JSON objects and returns a list of differences.
- `main() -> None`: The main function, handling user input and initiating the comparison process.

## Example Output

```
Differences found:
- Missing key1 in second JSON
- Different value at path.to.key: value1 vs value2
```

## Limitations

- The script assumes JSON files are located in the current working directory.
- It does not handle complex nested structures beyond dictionaries and lists.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests. Any contributions to enhance the functionality or efficiency of the script are welcome.

## License

This script is released under the MIT License. See the LICENSE file for more details.
