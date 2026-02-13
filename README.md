# panchakshari-oops

Student & Subject Management System

A simple Object-Oriented CRUD-based Student Management System built using Python.
This project demonstrates class inheritance, nested classes, UUID usage, and relationship mapping between Students and Subjects.

📌 Features
👨‍🎓 Student Management

Add Student

View Student (with assigned subjects)

Update Student details

Delete Student

View All Students

Assign Subjects to Student

📘 Subject Management

Add Subject(s)

View All Subjects

Delete Subject

The project uses:

CRUD → Base class containing common Create, Read, Update, Delete logic.

Student → Inherits from CRUD and manages student data.

Subject → Inherits from CRUD and manages subject data.

uuid → Generates unique IDs for subjects.

Concepts Used

Object-Oriented Programming (OOP)

Inheritance

Nested Classes

Dictionary-based storage

UUID generation

Class Design
🔹 CRUD (Base Class)

Provides:

create()

read()

update()

delete()

display_all()

Subject

Each subject gets a unique UUID.

Stored in dictionary using UUID as key.

🔹 Student

Stored using USN as key.

Each student contains:

name

usn

subject_ids (List of assigned subject UUIDs)

Data Storage

Data is stored in-memory using dictionaries

No database used

All data resets when program stops

Author
PAnchakshari Matada
