# api/view_counter.py
import json
import os

# This will store the views in a simple text file for now.
file_path = "/tmp/view_count.txt"

def handler(request):
    # Initialize view count file if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("0")
    
    # Read the current view count
    with open(file_path, "r") as f:
        view_count = int(f.read())

    # Increment the view count
    view_count += 1

    # Update the file with the new view count
    with open(file_path, "w") as f:
        f.write(str(view_count))

    # Return the updated view count in JSON format
    return {
        "statusCode": 200,
        "body": json.dumps({"view_count": view_count}),
        "headers": {
            "Content-Type": "application/json"
        }
    }
