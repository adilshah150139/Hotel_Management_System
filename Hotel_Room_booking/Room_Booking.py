class Hotel:
    def __init__(self):
        self.rooms = {
            101: None,
            102: None,
            103: None,
            104: None,
            105: None
        }
    def show_rooms(self):
        print("\nRoom Status: ")
        for room, guest in self.rooms.items():
            if guest is None:
                print(room, "-Available")
            else:
                print(f"{room}, -Booked by {guest.upper()} 🤩")

    def book_room(self, room, guest_name):
        if room in self.rooms and self.rooms[room] is None:
            self.rooms[room] = guest_name
            print("Room Successfully Booked! ✅")
        else:
            print("Room is Not Available.")

    def cancel_booking(self, room):
        if room in self.rooms and self.rooms[room] is not None:
            self.rooms[room] = None
            print("Room Successfully Canceled.✅")
        else: 
            print("Room is Already is Available.") 

hotel = Hotel()
while True:
    print("\n------------ Hotel Management System____________")
    print("\n1.Show Rooms\n2.Book Rooms\n3.Cancel Booking\n4.Exit")
    choice = input("Enter Your Choice: ")

    if choice == "1":
        hotel.show_rooms()
    elif choice == "2":
        room = int(input("Enter Room Number: "))
        name = input("Enter Guest Name: ")
        hotel.book_room(room, name)
    elif choice == "3":
        room = int(input("Enter Room Number: "))
        hotel.cancel_booking(room)
    elif choice == "4":
        print("Thanks, for Using Hotel Management System😊")
        break
    else:
        print("Invalid choice!")



