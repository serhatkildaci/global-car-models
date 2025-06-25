import json
import csv
import yaml
import os
import sys

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def read_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def read_csv(file_path):
    data = {}
    with open(file_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            brand, model = row
            if brand not in data:
                data[brand] = []
            data[brand].append(model)
    return data

def write_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, sort_keys=True)

def write_yaml(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, sort_keys=True)

def write_csv(data, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['brand', 'model'])
        for brand, models in sorted(data.items()):
            for model in sorted(models):
                writer.writerow([brand, model])

def main():
    trigger_file = os.getenv('TRIGGER_FILE')
    if not trigger_file:
        print("Error: TRIGGER_FILE environment variable not set.")
        sys.exit(1)

    print(f"Triggered by: {trigger_file}")

    base_path = 'data'
    json_file = os.path.join(base_path, 'models.json')
    csv_file = os.path.join(base_path, 'models.csv')
    yaml_file = os.path.join(base_path, 'models.yaml')

    data = None
    if trigger_file.endswith('.json'):
        data = read_json(trigger_file)
        print("Updating CSV and YAML from JSON...")
        write_csv(data, csv_file)
        write_yaml(data, yaml_file)
    elif trigger_file.endswith('.csv'):
        data = read_csv(trigger_file)
        print("Updating JSON and YAML from CSV...")
        write_json(data, json_file)
        write_yaml(data, yaml_file)
    elif trigger_file.endswith('.yaml'):
        data = read_yaml(trigger_file)
        print("Updating JSON and CSV from YAML...")
        write_json(data, json_file)
        write_csv(data, csv_file)
    else:
        print(f"Unsupported file type: {trigger_file}")
        sys.exit(1)

    print("Data synchronization complete.")

if __name__ == "__main__":
    main()
