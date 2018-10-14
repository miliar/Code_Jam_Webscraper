

import sys
input = sys.stdin



def add_to(d, key, value):
    if not d.has_key(key):
        d[key] = value
    else:
        d[key] += value


def solve(N, M, trips):
    update_points = set()
    for t in trips:
        update_points.add(t[0])
        update_points.add(t[1])
    ups = list(update_points)
    ups.sort()

    cost = 0

    train = []
    last_station = -1
    for station in ups:
        #Add distance.
        for i in range(len(train)):
            train[i][0] += station - last_station

        #Get on.
        for tr in trips:
            if tr[0] == station:
                train.append([0, tr[1], tr[2]])
        #Swap.
        passengers = {}
        tickets = {}
        for group in train:
            distance, getoff, n_people = group
            add_to(passengers, getoff, n_people)
            add_to(tickets, distance, n_people)
        ps = passengers.keys()
        ts = tickets.keys()
        ps.sort()
        ts.sort()
        new_train = []
        p = 0
        t = 0
        while p < len(ps) and t < len(ts):
            if 0 == passengers[ps[p]]:
                p += 1
                continue
            if 0 == tickets[ts[t]]:
                t += 1
                continue
            n_people = min(passengers[ps[p]], tickets[ts[t]])
            new_train.append([ts[t], ps[p], n_people])
            passengers[ps[p]] -= n_people
            tickets[ts[t]] -= n_people
        

        #Get off.
        train = []
        for group in new_train:
            distance, getoff, n_people = group
            if station != getoff:
                train.append(group)
            else:
                cost += n_people * (2*N + 1 - distance) * distance / 2
                


        last_station = station

    
    nominal_cost = 0
    for (a, b, np) in trips:
        dist = b - a
        nominal_cost += np * (2*N + 1 - dist) * dist / 2

    return (nominal_cost - cost) % 1000002013




T = int(input.readline())

for icase in range(1, T+1):
    N, M = map(int, input.readline().split())
    trips = []
    for i in range(M):
        trips.append(map(int, input.readline().split()))


    print "Case #%d:" % icase, solve(N, M, trips)
