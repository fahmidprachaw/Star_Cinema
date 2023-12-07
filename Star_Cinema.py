class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, row, col, hall_no):
        super().__init__()  
        self.row = row
        self.col = col
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []

        
        Star_Cinema.entry_hall(self, self)



    def entry_show(self, id, movie_name, time):
        movie = (id, movie_name, time)
        self.show_list.append(movie)

        self.seats[id] = [[0 for i in range(self.row)] for j in range(self.col)]



    def view_show_list(self):
        for show in self.show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def book_seats(self, id, want_seat):
        for row, col in want_seat:
            if self.seats[id][row][col] == 0:
                self.seats[id][row][col] = 1
                print('Boked')

            else:
                print('Alredy booked')


    def view_available_seats(self, id):
        flag = 0
        for i in self.show_list:
            if id == i[0]:
                flag = 1
                print(f'Avilable Seats for ID : {id}')
                for row in self.seats[id]:
                    for seat in row:
                        print(seat, end=' ')
                    print()
        if flag == 0:
            print('Please Provide Right ID')


h = Hall(5, 5, 3)
h.entry_show(1001, 'Home Alone', '10:30pm')
h.entry_show(1002, 'Home Alone 2', '1:00pm')
h.entry_show(1003, 'Animal', '4:30pm')
h.entry_show(1004, 'The Marvels', '10:30am')



text = """
    WELCOME TO STAR CINEMA

    1. VIEW ALL SHOW TODAY
    2. VIEW AVIALABLE SEATS
    3. BOOK TICKET
    4. EXIT
    
"""




def swith_case(num):
    match num:
        case 1:
            print(text)
            print()
            h.view_show_list()
        case 2:
            print(text)
            print()
            print("Please Enter the Movie ID : ", end=' ')
            input_id = int(input())
            h.view_available_seats(input_id)
        case 3:
            print(text)
            print()
            print("Please Enter the Movie ID : ", end=' ')
            input_id = int(input())
            print("Please Enter Seat Number([row][col])", end=' ')
            row, col = map(int, input().split())
            h.book_seats(input_id,[(row,col)])



print(text)

while True:
    user_input = int(input())
    swith_case(user_input)
    if user_input == 4:
        break
