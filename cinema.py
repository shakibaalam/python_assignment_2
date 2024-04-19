class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls._hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[id] = [['free' for _ in range(self._cols)] for _ in range(self._rows)]

    def book_seats(self, id, seat_list):
        if id not in [show[0] for show in self._show_list]:
            print("Invalid show ID")
            return

        for seat in seat_list:
            row, col = seat
            if row < 1 or row > self._rows or col < 1 or col > self._cols:
                print("Invalid seat")
                return
            if self._seats[id][row - 1][col - 1] == 'booked':
                print(f"Seat ({row}, {col}) is already booked")
                return
        for seat in seat_list:
            row, col = seat
            self._seats[id][row - 1][col - 1] = 'booked'
        print("Seats booked successfully!")

    def view_show_list(self):
        print("Shows running in this hall:")
        for show in self._show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, id):
        if id not in [show[0] for show in self._show_list]:
            print("Invalid show ID")
            return
        print("Available seats for this show:")
        for i in range(self._rows):
            for j in range(self._cols):
                if self._seats[id][i][j] == 'free':
                    print(f"Row: {i + 1}, Col: {j + 1}")


class Counter:
    def __init__(self):
        self._hall_list = Star_Cinema._hall_list

    def view_all_shows(self):
        print("All shows running:")
        for hall in self._hall_list:
            hall.view_show_list()

    def view_available_seats_in_show(self, hall_no, show_id):
        for hall in self._hall_list:
            if hall._hall_no == hall_no:
                hall.view_available_seats(show_id)
                return
        print("Invalid hall number")

    def book_tickets(self, hall_no, show_id, seat_list):
        for hall in self._hall_list:
            if hall._hall_no == hall_no:
                hall.book_seats(show_id, seat_list)
                return
        print("Invalid hall number")


# example :
hall1 = Hall(rows=5, cols=10, hall_no=1)
hall1.entry_show(id="show1", movie_name="Avengers", time="12:00 PM")
hall1.book_seats(id="show1", seat_list=[(1, 1), (2, 2)])
hall1.view_show_list()
hall1.view_available_seats(id="show1")


hall2 = Hall(rows=6, cols=8, hall_no=2)
hall2.entry_show(id="show2", movie_name="Inception", time="3:00 PM")
hall2.entry_show(id="show3", movie_name="The Godfather", time="6:00 PM")

hall3 = Hall(rows=7, cols=9, hall_no=3)
hall3.entry_show(id="show4", movie_name="The Shawshank Redemption", time="4:00 PM")
hall3.entry_show(id="show5", movie_name="The Dark Knight", time="7:00 PM")

# example of Counter
counter = Counter()
counter.view_all_shows()
counter.view_available_seats_in_show(hall_no=1, show_id="show1")
counter.view_available_seats_in_show(hall_no=2, show_id="show2")
counter.view_available_seats_in_show(hall_no=3, show_id="show4")

counter.book_tickets(hall_no=2, show_id="show3", seat_list=[(3, 4), (4, 5)])
counter.book_tickets(hall_no=3, show_id="show5", seat_list=[(2, 3), (3, 4), (5, 6)])

