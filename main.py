import csv
import time

# try modulo to keep the number from getting too large
# goal: decrease construction time
def myHash(key):
    total = 0
    for c in key:
        total = ((total << 5) + ord(c)) % 1000000007
    return total

# linear hash table
class HashTable:
    def __init__(self, capacity):
        self.collisions = 0
        self.capacity = capacity
        self.table = []
        for i in range(capacity):
            self.table.append(None)

    def hash(self, key):
        return myHash(key) % self.capacity

    def insert(self, key, value):
        index = self.hash(key)

        for step in range(self.capacity):
            slot = self.table[index]

            if slot is None or slot[0] == key:
                self.table[index] = (key, value)
                return

            # collision
            self.collisions += 1
            index = (index + 1) % self.capacity

    def wasted_space(self):
        empty = 0
        for slot in self.table:
            if slot is None:
                empty += 1
        return empty

class Movie:
    def __init__(self, row):
        data = row
        self.title = data[0]
        self.genre = data[1]
        self.date = data[2]
        self.director = data[3]
        self.revenue = data[4]
        self.rating = data[5]
        self.duration = data[6]
        self.company = data[7]
        self.quote = data[8]

################################################

with open("MOCK_DATA.csv", mode="r", encoding="utf-8", newline="") as file:
    reader = list(csv.reader(file))

    # skip header
    capacity = len(reader) - 1

    # construct byTitle table
    t0 = time.time_ns()

    byTitle = HashTable(capacity)

    for i in range(capacity):
        movie = Movie(reader[i+1])

        byTitle.insert(movie.title, movie)

    t1 = time.time_ns()

    # byTitle statistics
    wasted_space = byTitle.wasted_space()
    collisions = byTitle.collisions
    construction_time_ns = t1 - t0

    print(
        "-- Movies By Title Hash Statistics -- \n"+
        "Wasted Space: " + str(wasted_space) + "\n" +
        "Collisions: " + str(collisions) + "\n" +
        "Construction time (ns): " + str(construction_time_ns) + "\n"
    )



    # construct byQuote table
    t0 = time.time_ns()

    byQuote = HashTable(capacity)

    for i in range(capacity):
        movie = Movie(reader[i+1])

        byQuote.insert(movie.quote, movie)

    t1 = time.time_ns()

    # byQuote statistics
    wasted_space = byQuote.wasted_space()
    collisions = byQuote.collisions
    construction_time_ns = t1 - t0

    print(
        "-- Movies By Quote Hash Statistics -- \n"+
        "Wasted Space: " + str(wasted_space) + "\n" +
        "Collisions: " + str(collisions) + "\n" +
        "Construction time (ns): " + str(construction_time_ns) + "\n"
    )