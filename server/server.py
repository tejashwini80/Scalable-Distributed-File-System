from flask import Flask, request, jsonify
import os

app = Flask(__name__)
storage_dir = "storage"

# Ensure the storage directory exists
if not os.path.exists(storage_dir):
    os.makedirs(storage_dir)

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected for upload"}), 400
    file.save(os.path.join(storage_dir, file.filename))
    return jsonify({"message": f"File {file.filename} uploaded successfully!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


import logging

app.logger.setLevel(logging.DEBUG)

@app.before_request
def log_request_info():
    app.logger.debug(f"Request method: {request.method}")
    app.logger.debug(f"Request path: {request.path}")
