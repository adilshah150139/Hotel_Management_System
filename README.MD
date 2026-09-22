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

### Project-Structure
```
Hotel_Management_System/
|
|-- Hotel_Room_booking.py    # Main application file
|-- README.md                # Project documentation
```

--- 

## Requirements

- Python 3.14.3 or higher
- No external dependencies

To confirm Python is installed:

```bash
python --version
```

---

## Installation And Usage
```
git clone [https://github.com/adilshah150139/Hotel_Management_System.git](https://github.com/adilshah150139/Hotel_Management_System.git)
```
---

## How It Works

The application is built around a single `Hotel` class that manages room state using a dictionary.

- Each key in the dictionary is a room number (101, 102, 103).
- Each value is either `None` (available) or a guest name (booked).

The class provides three methods:

- `show_rooms()` — prints the status of every room
- `book_room(room, guest_name)` — books a room if it exists and is available
- `cancel_booking(room)` — frees a room if it is currently booked

The main program is a `while` loop that displays a menu, reads user input, and calls the appropriate method. The loop runs until the user chooses to exit.

---

## Example Session

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
Enter Guest Name: Shah
Room Successfully Booked! ✅
```

---

## Future Improvements

- Add input validation with `try/except` to handle non-numeric room input without crashing.
- Persist bookings to a JSON file so data survives between sessions.
- Allow rooms to be added or removed dynamically instead of hardcoding 101, 102, 103.
- Add check-in and check-out dates to each booking.
- Introduce a `Guest` class to store additional details such as phone number and email.
- Write unit tests using `unittest` to cover booking, cancellation, and edge cases.
- Refactor the menu into a separate `main()` function for cleaner structure.
