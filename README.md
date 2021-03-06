# PESU-APP

This is a complete web application developed using Flask for the backend and MySQL for the database. Iterative + Incremental SDLC model was used to develop the project.

## How to run

Open a terminal on Linux/WSL. Run the following:
```bash
git clone https://github.com/sreyansb/PESU_APP.git
cd PESU_APP
python mainapp.py
```

## Features

- Login functionality with 3 types of users (Admin, Faculty, Student)
- Admin Features:
    - Course content management (View, Add, Edit courses)
    - Event notification system (View, Add, Edit, delete notifications)
    - Student profiles (View, Add, Edit student profiles)
    - Faculty profiles (View, Add, Edit faculty profiles)
    - Course feedback (View all subjects feedback)
- Faculty Features:
    - Course content dashboard (View course details that are taught)
    - Notification system (View all notifications)
- Student Features:
    - Course content dashboard (View course details that are opted for)
    - Notification system (View all notifications)
    - Course feedback (Give feedback to courses opted for)

## Design Diagrams

### 1. Class Diagram
<p align="center">
	<kbd><img src="./images/1. Class Diagram.jpg" width="500px"></kbd>
</p>

### 2. System Architecture
<p align="center">
	<kbd><img src="./images/2. System Architecture.jpg" width="500px"></kbd>
<p>

For the other activity diagrams and sequence diagrams for each use case, refer to the `images/` folder.

## Screenshots

<p align="center">
	<kbd><img src="./images/s1.login.png" width="500px"></kbd>
	<kbd><img src="./images/s2.notifications.png" width="500px"></kbd>
	<kbd><img src="./images/s3.feedback.png" width="500px"></kbd>
	<kbd><img src="./images/s4.students.png" width="500px"></kbd>
</p>

## Info
This project was done as part of our Object Oriented Analysis and Design course.

## Team
- Sahith Kurapati - [@Sahith02]( https://github.com/Sahith02 )
- Revanth Babu PN - [@RevanthBabuPN]( https://github.com/RevanthBabuPN )
- Sreyans Bothra - [@sreyansb]( https://github.com/sreyansb )
