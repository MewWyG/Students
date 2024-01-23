from flask import request, Flask, jsonify

app = Flask(__name__)
students = [
    {"id": 6530300660, "name": "Apiwit Nares", "major": "T12", "gpa": "2.93"},
    {"id": 6630322211, "name": "Somchai Jaidee", "major": "T12", "gpa": "3.3"},
    {"id": 6630322212, "name": "Sommai Jaidee", "major": "T22", "gpa": "1.5"},
    {"id": 6530300661, "name": "Tiwipa Nares", "major": "T17", "gpa": "3.5"},
]

@app.route("/")
def Greet():
    return "<p>Welcome to Student Management API</p>"

@app.route("/std", methods=["GET"])
def get_all_std():
    return jsonify({"students": students})

@app.route("/std/<int:student_id>", methods=["GET"])
def get_std(student_id):
    std = next((b for b in students if b["id"] == student_id), None)
    if std:
        return jsonify(std)
    else:
        return jsonify({"error": "Student not found"}), 404

@app.route("/std", methods=["POST"])
def create_std():
    data = request.get_json()
    new_std = {
        "id": data["id"],
        "name": data["name"],
        "major": data["major"],
        "gpa": data["gpa"],
    }
    students.append(new_std)
    return jsonify(new_std), 201

@app.route("/std/<int:student_id>", methods=["DELETE"])
def delete_std(student_id):
    global students
    students = [b for b in students if b["id"] != student_id]
    return jsonify({"message": "Student deleted successfully"})

@app.route("/std/<int:student_id>", methods=["PUT"])
def update_std(student_id):
    std = next((b for b in students if b["id"] == student_id), None)
    if std:
        data = request.get_json()
        std.update({
            "name": data["name"],
            "major": data["major"],
            "gpa": data["gpa"],
        })
        return jsonify(std)
    else:
        return jsonify({"error": "Student not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
