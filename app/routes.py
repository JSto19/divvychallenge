from app import app, db
from flask import render_template, request
from app.models import Divvy

@app.route('/')
@app.route('/index')
def not_yet():
    return render_template('index.html')

@app.route('/calc')
def calc():
    req = request.args.to_dict()
    start_time = req['start']
    stop_time = req['end']
    averagetime = 0
    totaltime = 0
    divvy = Divvy.query.filter(Divvy.starttime.between(starttime, stoptime)).all()
    length = len(divvy)
    for i in range(length):
        totaltime = totaltime + divvy[i].trip_duration
    averagetime = totaltime / length
    return {'averagetime': averagetime}