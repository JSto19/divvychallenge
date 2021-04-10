from app import db
from datetime import datetime

class Divvy(db.Model):
    trip_id = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.DateTime(), nullable = False)
    stop_time = db.Column(db.DateTime(), nullable = False)
    bike_id = db.Column(db.Integer, nullable = False)
    from_station_id = db.Column(db.Integer, nullable = False)
    from_station_name = db.Column(db.String, nullable = False)
    to_station_id = db.Column(db.Integer, nullable = False)
    to_station_name = db.Column(db.String, nullable = False)
    usertype = db.Column(db.String, nullable = False)
    gender = db.Column(db.String(150), nullable = True)
    birthday = db.Column(db.String(150), nullable = True)
    trip_duration = db.Column(db.Integer, nullable = False)

    def __init__ (self, name, number, email, address, user_id):
        self.trip_id = trip_id
        self.start_time = start_time 
        self.stop_time = stop_time
        self.bike_id = bike_id
        self.from_station_id = from_station_id
        self.from_station_name = from_station_name
        self.to_station_id = to_station_id 
        self.to_station_name = to_station_name
        self.usertype = usetype
        self.gender = gender
        self.birthday = birthday
        self.trip_duration = trip_duration
    