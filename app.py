from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Scientist',
    'location': 'Durban',
    'salary': 'R 30 000 pm'
}, {
    'id': 2,
    'title': 'Data Engineer',
    'location': 'Gauteng',
    'salary': 'R 32 000 pm'
}, {
    'id': 3,
    'title': 'Full Stack Engineer',
    'location': 'Cape Town',
    'salary': 'R 27 000 pm'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
