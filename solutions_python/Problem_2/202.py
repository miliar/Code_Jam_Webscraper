from datetime import datetime, time, timedelta

def add_time(value, T):
    departure = datetime.combine(datetime.today(), time(int(value[0:2]), int(value[3:])))
    ready = departure + timedelta(minutes=T)
    if ready.date() == departure.date():
        return ready.strftime("%H:%M")
    return "99:99" # Too long to wait, the departure is not today

def insert_train(trains, train, i):
    if i == len(trains) - 1: return i + 1
    if train > trains[-1]: return len(trains)
    j = i + 1
    k = len(trains) - 1
    while True:
        if j >= k - 1:
            if train > trains[j]:
                return j + 1
            return j
        l = (j+k)//2
        if trains[l] >= train: k = l
        else: j = l 

def send_train(trains, T, i):
    train = trains[i]
    arrival = train[6:11]
    # Construct the new train line.
    new_train = add_time(arrival, T) + " "*7
    if train[-1] == "A": new_train += "B"
    else: new_train += "A"
    # Insert this line into the list.
    trains.insert(insert_train(trains, new_train, i), new_train)
    return trains

def solve(trains, T):
    max_a, max_b = 0, 0
    cur_a, cur_b = 0, 0
    i = 0
    while i < len(trains):
        train = trains[i] # train is a string: "HH:MM HH:MM X"
        if train[6:11] == " "*5:
            # This train came from the other station.
            if train[-1] == "A": cur_a += 1
            else: cur_b += 1
        else:
            # This train must go on schedule.
            if train[-1] == "A":
                if cur_a > 0: cur_a -= 1
                else: max_a += 1
            else:
                if cur_b > 0: cur_b -= 1
                else: max_b += 1
            trains = send_train(trains, T, i)
        i += 1
    return (max_a, max_b)

f = open("b-large.txt")
N = int(f.readline())
for n in range(0, N):
    T = int(f.readline())
    NAB = f.readline().split()
    NA = int(NAB[0])
    NB = int(NAB[1])
    trains = [f.readline().rstrip() + " A" for i in range(0, NA)]
    trains += [f.readline().rstrip() + " B" for i in range(0, NB)]
    trains.sort()
    print("Case #%d: %d %d" % ((n + 1,) + solve(trains, T)))

