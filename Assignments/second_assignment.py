"""MOVIE TICKET BOOKING"""

Movie_shows = {
    "Skybound":{
        "time":"10:30 am",
        "price":180,
        "seats":30
    },
    "The last signal":{
         "time":"2:00 pm",
        "price":220,
        "seats":25
    },
     "ocean mystery": {
        "time": "6:30 PM",
        "price": 200,
        "seats": 20
}
}

bookings =[]
booking_num = 1

def list_shows():
    print("/////////// Available Shows /////////////")
    sorted_show = sorted(Movie_shows.items(),key=lambda item:item[1]["price"])
    print("Movie  Time   Price   Seats")
    for movie, details in sorted_show:
        print(movie, details["time"],details["price"],details["seats"])

def calculate(*prices, discount=0):
    original_total = sum(prices)
    discount_amount = original_total * discount / 100
    final_total = original_total - discount_amount
    return original_total, discount_amount, final_total

def book_tickets(show_name, num_of_tickets, loyal_member=False):
    global booking_num
    if show_name not in Movie_shows:
        print("Movies not found")
        return
    
    if num_of_tickets <= 0:
        print("Enter a valid number of ticket ")
        return
    
    available_seats = Movie_shows[show_name]["seats"]
    if num_of_tickets > available_seats:
        print("Failed Booking ")
        return
    
    price = Movie_shows[show_name]["price"]
    discount = 0
    if num_of_tickets >= 5:
        discount = 10
    if loyal_member:
        discount = 15
        
    original, discount_amt, final = calculate(*([price] * num_of_tickets), discount=discount)
        
    booking_id = "PVR" + str(booking_num)
    booking_details ={
        "id":booking_id,
        "movie": show_name,
        "time": Movie_shows[show_name]["time"],
        "tickets": num_of_tickets,
        "original": original,
        "discount":discount,
        "discount_amount": discount_amt,
        "total": final,
        "status":"confirmed"
    }
    bookings.append(booking_details)
    Movie_shows[show_name]["seats"] -= num_of_tickets
    booking_num += 1
    print("Booking successful")
    print("Booking id:", booking_id)
    print("Movie:",show_name)
    print("Showtime:",Movie_shows[show_name]["time"])
    print("Tickets:",num_of_tickets)
    print("Original total:",original)
    print("Discount applied",discount)
    print("Discount amount:",discount_amt)
    print("Final amount:", final)
    print("Seats remaining:", Movie_shows[show_name]["seats"])

def view_bookings():
    print("-------Booking Details---------")
    if len(bookings) == 0:
        print("No bookings found.")
        return
    for details in bookings:
            print("Booking ID:", details["id"])
            print("Movie:", details["movie"])
            print("Showtime:", details["time"])
            print("Tickets:", details["tickets"])
            print("Total amount:", details["total"])
            print("Status:", details["status"])

def cancel_booking(booking_id):
     for details in bookings:
          if details["id"] == booking_id:
              if details["status"] == "Cancelled":
                print("Booking already cancelled!")
                return
              details["status"] = "Cancelled"
              Movie_shows[details["movie"]]["seats"] += details["tickets"] 
              print("Booking cancelled successfully")
              print("Refund amount:", details["total"])
              print("Seats restored:", details["tickets"])
              return
          print("Booking ID not found")

while True:
    print("----------MOVIE TICKET BOOKING -----------")
    print("1. List Available Shows")
    print("2. Book Tickets")
    print("3. View Bookings")
    print("4. Cancel Booking")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        list_shows()
        
    elif choice == "2":
        list_shows()
        movie = input("Enter movie name: ")
        quantity_input = input("Enter number of tickets ")

        if quantity_input.isdigit():
            quantity = int(quantity_input)
            member = input("Are you a loyality member? yes/no : ")
            
            if member not in ["yes", "no"]:
                print("Please enter yes or no.")
            else:
                book_tickets(movie,quantity,loyal_member=(member == "yes")
                )
        else:
            print("Please enter a valid whole number.")
    elif choice == "3":
        view_bookings()

    elif choice == "4":
        booking_id = input("Enter booking ID: ")
        cancel_booking(booking_id)

    elif choice == "5":
        print("Thank you ")
        break

    else:
        print("Invalid choice! Select an option from 1 to 5.")






















