from flask import Flask,jsonify

app = Flask(__name__)
students=[
    {"id":6530300660,"Name":"Apiwit Nares","Major":"T12","GPA":"2.93"},
    {"id":2,"title":"Book 2","author":"Author 2"},
    {"id":3,"title":"Book 3","author":"Author 3"},
    {"id":4,"title":"Book 4","author":"Author 4"},
]

@app.route("/")
def Greet():
    return "<p>Welocome to back Management System</p>"

@app.route("/std",methods = [("GET")])
def get_all_std():
    return jsonify({"student:":students})

@app.route("/std/<int:student_id>",methods=["GET"])
def get_std(student_id):
    students=next((b for b in students if b["id"]==student_id),None)
    if students:
        return jsonify(students)
    else:
        return jsonify({"error":"Student not found"}),404

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)