HOME.HTML :-
</body>
</html><!doctype html>
<html lang="en">
<style type='text/css'>
* {
padding: 0;
margin: 0;
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
body {
background-image: url('https://cdn.pixabay.com/photo/2018/12/18/22/29/background-
3883181_1280.jpg');
background-size: cover; 
font-family: sans-serif; 
margin-top: 40px; 
height: 100vh;
padding: 0;
margin: 0;
}
table {
border: 1px;
font-family: arial, sans-serif; 
border-collapse: collapse; 
width: 86%;
margin: auto;
}
td,
th {
border: 1px solid black !important; 
padding: 5px;
} 20 21
tr:nth-child(even) { 
background-color: #dddddd;
}
</style>
<head>
<!-- Required meta tags-->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
<!-- Bootstrap CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" 
integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
crossorigin="anonymous">
<title>Face Recognition Based Attendance System</title>
</head>
<body>
<div class='mt-3 text-center'>
<h1 style="width: auto;margin: auto;color: white;padding: 11px;font-size: 44px;">Face Recognition 
Based Attendance System</h1>
</div>
{% if mess%}
<p class="text-center" style="color: red;font-size: 20px;">{{ mess }}</p>
{% endif %}
<div class="row text-center" style="padding: 20px;margin: 20px;">
<div class="col"
style="border-radius: 20px;padding: 0px;background-color:rgb(211,211,211,0.5);margin:0px 10px 
10px 10px;min-height: 400px;"> 21
<h2 style="border-radius: 20px 20px 0px 0px;background-color: #0b4c61;color: white;padding: 
10px;">Today's
Attendance <i class="material-icons">assignment</i></h2>
<a style="text-decoration: none;max-width: 300px;" href="/start">
<button
style="font-size: 24px;font-weight: bold;border-radius: 10px;width:490px;padding: 10px;margin-
top: 30px;margin-bottom: 30px;"
type='submit' class='btn btn-primary'>Take Attendance <i 
class="material-icons">beenhere</i></button>
</a>
<table style="background-color: white;">
<tr>
<td><b>S No</b></td>
<td><b>Name</b></td>
<td><b>ID</b></td>
<td><b>Time</b></td>
</tr>
{% if l %}
{% for i in range(l) %}
<tr>
<td>{{ i+1 }}</td>
<td>{{ names[i] }}</td>
<td>{{ rolls[i] }}</td>
<td>{{ times[i] }}</td>
</tr>
{% endfor %}
{% endif %}
</table>
</div>
<div class="col"
style="border-radius: 20px;padding: 0px;background-color:rgb(211,211,211,0.5);margin:0px 10px 
10px 10px;height: 400px;">
<form action='/add' method="POST" enctype="multipart/form-data">
<h2 style="border-radius: 20px 20px 0px 0px;background-color: #0b4c61;color: white;padding: 
10px;">Add 22
New User <i class="material-icons">control_point_duplicate</i></h2>
<label style="font-size: 20px;"><b>Enter New User Name*</b></label>
<br>
<input type="text" id="newusername" name='newusername'
style="font-size: 20px;margin-top:10px;margin-bottom:10px;" required>
<br>
<label style="font-size: 20px;"><b>Enter New User Id*</b></label>
<br>
<input type="number" id="newusereid" name='newuserid'
style="font-size: 20px;margin-top:10px;margin-bottom:10px;" required>
<br>
<button style="width: 232px;margin-top: 20px;font-size: 20px;" type='submit' class='btn btn-
dark'>Add
New User
</button>
<br>
<h5 style="padding: 25px;"><i>Total Users in Database: {{totalreg}}</i></h5>
</form>
</div>
</div> 23
INDEX.HTML :-
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!--=============== REMIXICONS ===============-->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/remixicon@2.5.0/fonts/remixicon.css">
<!--=============== CSS ===============-->
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<title>Animated login form</title>
</head>
<body>
<div class="login">
<img src="{{ url_for('static', filename='love.jpg') }}" alt="login image" class="login img">
<form action="/login" method="POST" class="container" id="loginForm">
<h1 class="login title">Get Started</h1>
<div class="login content">
<div class="login box">
<i class="ri-user-3-line login icon"></i>
<div class="login box-input">
<input type="email"name="email" required class="login input" id="login-email" 
placeholder=" ">
<label for="login-email" class="login label">Username</label>
</div>
</div>
<div class="login box"> 24
<i class="ri-lock-2-line login icon"></i>
<div class="login box-input">
<input type="password" name="password" required class="login input" id="login-pass" 
placeholder=" ">
<label for="login-pass" class="login label">Password</label>
<i class="ri-eye-off-line login eye" id="login-eye" onclick="togglePasswordVisibility()"></i>
</div>
</div>
</div>
<div class="login check">
<div class="login check-group">
<input type="checkbox" class="login check-input" id="login-check">
<label for="login-check" class="login check-label">Remember me</label>
</div>
<a href="#" class="login forgot">Forgot Password?</a>
</div>
<button type="submit" class="login button">Login</button>
<p class="login register">
Don't have an account? <a href="{{ url_for('register') }}">Register</a>>
</p>
</form>
</div>
<script>
// Toggle password visibility
function togglePasswordVisibility() {
const passwordField = document.getElementById('login-pass'); 
const eyeIcon = document.getElementById('login-eye');
if (passwordField.type === 'password') { 
passwordField.type = 'text'; 
eyeIcon.classList.remove('ri-eye-off-line'); 
eyeIcon.classList.add('ri-eye-line');
} else { passwordField.type = 'password'; 
eyeIcon.classList.remove('ri-eye-line'); 
eyeIcon.classList.add('ri-eye-off-line');
}
}
// Form validation
const loginForm = document.getElementById('loginForm'); 
loginForm.addEventListener('submit', function (event) {
const email = document.getElementById('login-email').value; 
const password = document.getElementById('login-pass').value;
// Basic validation
if (email === '' || password === '') { 
event.preventDefault(); 
alert('Please fill out all fields');
} else {
alert('Form submitted successfully');
}
});
</script>
</body>
</html>
25 26
REGISTER.HTML :-
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="{{ url_for('static', filename='style1.css') }}">
<title>Register</title>
<!-- Add your CSS and necessary links -->
</head>
<body>
<div class="register">
<h1>Create New Account</h1>
<form action="">
<label for="username">Username:</label>
<input type="text" id="username" required><br><br>
<label for="email">Email:</label>
<input type="email" id="email" required><br><br>
<label for="password">Password:</label>
<input type="password" id="password" required><br><br>
<button type="submit">Register</button>
</form>
<p>Already have an account? <a href="{{ url_for('index') }}">Login here</a></p>
</div></body>
</html> 27
APP.PY :-
import os 
import cv2
import numpy as np 
import pandas as pd 
import joblib
from datetime import date, datetime
from flask import Flask, request, render_template, redirect, url_for, flash, session 
from sklearn.neighbors import KNeighborsClassifier
app = Flask(_name_)
app.secret_key = 'your_secret_key' # Replace with a random secret key for session management
VALID_USER = {
'email': 'bhaskar050903@gmail.com',
'password': 'b@030905'
}
nimgs = 10
imgBackground = cv2.imread(r'C:\Users\bhask\OneDrive\Documents\login page\background.png') 
datetoday = date.today().strftime("%m_%d_%y")
datetoday2 = date.today().strftime("%d-%B-%Y")
face_detector = cv2.CascadeClassifier(r'C:\Users\bhask\OneDrive\Documents\login 
page\haarcascade_frontalface_default.xml')
# Create necessary directories
if not os.path.isdir(r'C:\Users\bhask\OneDrive\Documents\login page\Attendance'): 
os.makedirs(r'C:\Users\bhask\OneDrive\Documents\login page\Attendance')
if not os.path.isdir(r'C:\Users\bhask\OneDrive\Documents\login page\static'): 
os.makedirs(r'C:\Users\bhask\OneDrive\Documents\login page\static')
if not os.path.isdir(r'C:\Users\bhask\OneDrive\Documents\login page\static\faces'): 
os.makedirs(r'C:\Users\bhask\OneDrive\Documents\login page\static\faces')
if f'Attendance-{datetoday}.csv' not in os.listdir(r'C:\Users\bhask\OneDrive\Documents\login 
page\Attendance'): with open(f'C:\\Users\\bhask\\OneDrive\\Documents\\login page\\Attendance\\Attendance-
{datetoday}.csv', 'w') as f: 
f.write('Name,Roll,Time')
def totalreg():
return len(os.listdir(r'C:\Users\bhask\OneDrive\Documents\login page\static\faces'))
def extract_faces(img): 
try:
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_points = face_detector.detectMultiScale(gray, 1.2, 5, minSize=(20, 20)) 
return face_points
except:
return []
def identify_face(facearray):
model = joblib.load(r'C:\Users\bhask\OneDrive\Documents\login page\static\face_recognition_model.pkl') 
return model.predict(facearray)
deftrain_model(): 
faces = []
labels = []
userlist = os.listdir(r'C:\Users\bhask\OneDrive\Documents\login page\static\faces')
for user in userlist:
for imgname in os.listdir(f'static/faces/{user}'):
img = cv2.imread(f'static/faces/{user}/{imgname}') 
resized_face = cv2.resize(img, (50, 50)) 
faces.append(resized_face.ravel()) 
labels.append(user)
faces = np.array(faces)
knn = KNeighborsClassifier(n_neighbors=5) 
knn.fit(faces, labels)
joblib.dump(knn, r'C:\Users\bhask\OneDrive\Documents\login page\static\face_recognition_model.pkl')
def extract_attendance():
df = pd.read_csv(f'C:\\Users\\bhask\\OneDrive\\Documents\\login page\\Attendance\\Attendance-
{datetoday}.csv') 28 29
names = df['Name'] 
rolls = df['Roll'] 
times = df['Time']
l = len(df)
return names, rolls, times, l
def add_attendance(name): 
username = name.split('_')[0] 
userid = name.split('_')[1]
current_time = datetime.now().strftime("%H:%M:%S")
df = pd.read_csv(f'C:\\Users\\bhask\\OneDrive\\Documents\\login page\\Attendance\\Attendance-
{datetoday}.csv')
if int(userid) not in list(df['Roll']):
with open(f"C:\\Users\\bhask\\OneDrive\\Documents\\login page\\Attendance\\Attendance-
{datetoday}.csv", 'a') as f: 
f.write(f'\n{username},{userid},{current_time}')
@app.route('/') 
def index():
return render_template('index.html') 
@app.route('/register')
def register():
return render_template('register.html') # Make sure thisfile exists
@app.route('/home') 
def home():
if not session.get('logged_in'): 
return redirect(url_for('login'))
names, rolls, times, l = extract_attendance()
return render_template('home.html', names=names, rolls=rolls, times=times, l=l, totalreg=totalreg(), 
datetoday2=datetoday2)
@app.route('/login', methods=['GET', 'POST']) 
def login():
if request.method == 'POST': 
email = request.form['email'] 30
password = request.form['password']
# Simple authentication logic
if email == VALID_USER['email'] and password == VALID_USER['password']: 
session['logged_in'] = True # Set session variable
return redirect(url_for('home')) 
else:
flash('Invalid Credentials! Please try again.', 'danger') 
return render_template('home.html')
return render_template('index.html')
def getallusers():
userlist = os.listdir(r'C:\Users\bhask\OneDrive\Documents\login page\static\faces\\') 
names = []
rolls = []
l = len(userlist) 
for i in userlist:
name, roll = i.split('_') 
names.append(name) 
rolls.append(roll)
return userlist, names, rolls, l
# @app.route('/home') 
# def home():
# if not session.get('logged_in'):
# return redirect(url_for('login'))
# names, rolls, times, l = extract_attendance()
# return render_template('home.html', names=names, rolls=rolls, times=times, l=l, totalreg=totalreg(), 
datetoday2=datetoday2)
@app.route('/start', methods=['GET']) 
def start():
names, rolls, times, l = extract_attendance()
if 'face_recognition_model.pkl' not in os.listdir('static'):
return render_template('home.html', totalreg=totalreg(), datetoday2=datetoday2, mess='There is no 
trained model in the static folder. Please add a new face to continue.') 31
ret = True
cap = cv2.VideoCapture(0) 
while ret:
ret, frame = cap.read()
if len(extract_faces(frame)) > 0:
(x, y, w, h) = extract_faces(frame)[0] 
cv2.rectangle(frame, (x, y), (x+w, y-40), (86, 32, 251), -1)
face = cv2.resize(frame[y:y+h, x:x+w], (50, 50)) 
identified_person = identify_face(face.reshape(1, -1))[0] 
add_attendance(identified_person)
cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
cv2.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 1)
imgBackground[162:162 + 480, 55:55 + 640] = frame 
cv2.imshow('Attendance', imgBackground)
if cv2.waitKey(1) == 32: 
break
cap.release() 
cv2.destroyAllWindows()
names, rolls, times, l = extract_attendance()
return render_template('home.html', names=names, rolls=rolls, times=times, l=l, totalreg=totalreg(), 
datetoday2=datetoday2)
@app.route('/add', methods=['GET', 'POST']) 
def add():
if request.method == 'POST':
newusername = request.form['newusername'] 
newuserid = request.form['newuserid']
userimagefolder = os.path.join(r'C:\Users\bhask\OneDrive\Documents\login page\static\faces', 
f'{newusername}_{newuserid}')
if not os.path.isdir(userimagefolder): 
os.makedirs(userimagefolder)
i, j = 0, 0 32
cap = cv2.VideoCapture(0) 
while True:
ret, frame = cap.read()
faces = extract_faces(frame)
# Check if any face is detected 
for (x, y, w, h) in faces:
cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.putText(frame, f'Images Captured: {i}/{nimgs}', (30, 30),
cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 20), 2, cv2.LINE_AA)
# Save image only if faces are detected 
if j % 5 == 0:
imgname = f"{newusername}{newuserid}{i}.jpg" 
# Ensure (x, y, w, h) are defined
cropped_face = frame[y:y+h, x:x+w] 
if cropped_face.size > 0:
cv2.imwrite(os.path.join(userimagefolder, imgname), cropped_face)
i += 1
j += 1
if j == nimgs * 5: 
break
cv2.imshow('Adding new User', frame)
if cv2.waitKey(1) == 32: # Space key to break 
break
cap.release() 
cv2.destroyAllWindows() 
print('Training Model') 
train_model()
names, rolls, times, l = extract_attendance()
return render_template('home.html', names=names, rolls=rolls, times=times, l=l, totalreg=totalreg(), 
datetoday2=datetoday2)
if _name_ == '_main_': 
app.run(debug=True) 9. Project Limitations and Future Scope
• Limitations:
o Accuracy limitations in challenging conditions (poor lighting, 
occlusions, facial hair).
o Dependence on high-quality hardware and sufficient processing 
power.
o Potential for bias in face recognition algorithms.
o Privacy and ethical considerations regarding data collection and 
usage.
• Future Scope:
o Integration with existing school management systems or HR 
platforms.
o Development of a mobile application for on-the-go attendance 
tracking.
o Exploration of more advanced deep learning models (e.g., 
Transformers).
o Implementation of multi-factor authentication (e.g., face recognition
+ PIN).
o Research and development of more r