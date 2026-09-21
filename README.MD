# Hotel Booking System

A command-line hotel room booking system built with Python. This project demonstrates core Object-Oriented Programming concepts including classes, methods, and state management through a simple interactive menu.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Installation and Usage](#installation-and-usage)
- [How It Works](#how-it-works)
- [Example Session](#example-session)
- [Future Improvements](#future-improvements)

---

## Overview

This project is a simple hotel management system that runs in the terminal. It allows a user to check room availability, book a room for a guest, and cancel an existing booking. The system is built around a single `Hotel` class that manages room state using a dictionary, where each room number maps to either a guest name or `None` if the room is available.

The project was built to practice:
- Object-Oriented Programming in Python
- Working with dictionaries and conditional logic
- Handling user input in a loop
- Structuring a small application with clear responsibilities

---

## Features

- View the current status of all rooms (available or booked)
- Book an available room by entering a room number and guest name
- Cancel a booking to make the room available again
- Menu-driven interface that runs until the user chooses to exit
- Basic validation to prevent double-booking and invalid operations

---

## Example-Session

------------ Hotel Management System____________

```
1. Show Rooms
2. Book Rooms
3. Cancel Booking
4. Exit
Enter Your Choice: 1

Room Status: 
101 - Available
102 - Available
103 - Available

Enter Your Choice: 2
Enter Room Number: 101
Enter Guest Name: Alice
Room Successfully Booked! ✅
```

## Requirements

- Python 3.14.3 or higher
- No external dependencies

To confirm Python is installed:

```bash
python --version
```

---

### Project-Structure
```
03_Hotel_Management_system/Room_Booking
|
|-- Hotel_Room_booking.py    # Main application file
|-- README.md                # Project documentation
```

--- 

## Installation-And-Usage
```
git clone [https://github.com/adilshah150139/Hotel_Management_System.git](https://github.com/adilshah150139/Hotel_Management_System.git)
```
