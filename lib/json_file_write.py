import json
import os
import time

def json_file_write(filename, data):
    now_timestamp = str(int(time.time()))
    os.makedirs("output", exist_ok=True)
    filepath = os.path.join("output", f"{filename}_{now_timestamp}.json")
    with open(filepath, "w", encoding="utf-8-sig") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"file path : {filepath}")
