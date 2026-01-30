from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Software Engineer",
        "location": "Remote",
        "salary": "$120,000 - $150,000"
    },
    {
        "id": 2,
        "title": "Product Manager",
        "location": "New York, NY",
        "salary": "$130,000 - $160,000"
    },
    {
        "id": 3,
        "title": "Data Scientist",
        "location": "San Francisco, CA",
        "salary": "$140,000 - $180,000"
    },
    {
        "id": 4,
        "title": "UX Designer",
        "location": "Remote",
        "salary": "$90,000 - $120,000"
    }
]


@app.route("/")
def home():
    return render_template("home.html", jobs=JOBS)


@app.route("/job/<int:job_id>")
def job_detail(job_id):
    job = next((j for j in JOBS if j["id"] == job_id), None)
    return render_template("job.html", job=job)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
