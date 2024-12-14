import os
import requests

SERVER_URL = "http://127.0.0.1:5000"

def upload_file(file_path):
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            response = requests.post(f"{SERVER_URL}/upload", files=files)
        print(response.json())
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def download_file(filename):
    response = requests.get(f"{SERVER_URL}/download/{filename}")
    print(response.json())

if __name__ == "__main__":
    action = input("Enter action (upload/download): ").strip().lower()
    if action == "upload":
        file_path = input("Enter file path: ").strip()
        if os.path.exists(file_path):
            upload_file(file_path)
        else:
            print(f"Error: The file '{file_path}' does not exist.")
    elif action == "download":
        filename = input("Enter filename: ").strip()
        download_file(filename)
    else:
        print("Invalid action. Please enter 'upload' or 'download'.")
