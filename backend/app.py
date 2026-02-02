from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Temporary in-memory database
issues = []

@app.route("/")
def home():
    return "CivicEye Backend Running"

@app.route("/add-issue", methods=["POST"])
def add_issue():
    data = request.json

    description = data.get("description", "").lower()
    if "pothole" in description or "accident" in description:
        priority = "High"
    else:
        priority = "Normal"

    issue = {
        "description": data.get("description"),
        "location": data.get("location"),
        "status": "Pending",
        "priority": priority
    }

    issues.append(issue)
    return jsonify({"message": "Issue added successfully"})

@app.route("/issues", methods=["GET"])
def get_issues():
    return jsonify(issues)

@app.route("/update-status", methods=["POST"])
def update_status():
    index = request.json.get("index")
    status = request.json.get("status")

    if index is not None and index < len(issues):
        issues[index]["status"] = status
        return jsonify({"message": "Status updated"})
    else:
        return jsonify({"message": "Invalid issue index"}), 400

if __name__ == "__main__":
    app.run(debug=True)
