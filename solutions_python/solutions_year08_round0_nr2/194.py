#!/usr/bin/python
''' Train Timetable
Google Code Jam 2008
Qualification Round - Problem B
Grant Glouser <gglouser@gmail.com>
'''

import sys

def read_int_line(f):
    return int(f.readline().rstrip())

def read_na_nb(f):
    na_nb = f.readline().rstrip()
    (na,nb) = na_nb.split()
    return (int(na),int(nb))

def time_to_minutes(time):
    (hr,min) = time.split(':')
    return int(hr) * 60 + int(min)

def read_trips(f, num_trips):
    trips = []
    for i in range(num_trips):
        trip = f.readline().rstrip()
        (dep,arr) = trip.split()
        trips.append((time_to_minutes(dep), time_to_minutes(arr)))
    return trips

def count_trains(departures, arrivals):
    trains = 0
    need = 0
    while departures:
        if not arrivals or departures[0] < arrivals[0]:
            if trains == 0:
                need += 1
            else:
                trains -= 1
            #print 'train leaving ... %2d %2d' % (trains,need)
            departures.pop(0)
        else:
            trains += 1
            #print 'train arriving .. %2d %2d' % (trains,need)
            arrivals.pop(0)
    return need

def do_test_case(f, case_num):
    turn_around_time = read_int_line(f)
    (na,nb) = read_na_nb(f)
    
    ab_trips = read_trips(f, na)
    ba_trips = read_trips(f, nb)
    
    a_deps = [d for (d,a) in ab_trips]
    a_deps.sort()
    a_arrs = [(a + turn_around_time) for (d,a) in ba_trips]
    a_arrs.sort()
    b_deps = [d for (d,a) in ba_trips]
    b_deps.sort()
    b_arrs = [(a + turn_around_time) for (d,a) in ab_trips]
    b_arrs.sort()
    #print 'station A departures:', a_deps
    #print 'station A arrivals:', a_arrs
    #print 'station B departures:', b_deps
    #print 'station B arrivals:', b_arrs
    a_trains = count_trains(a_deps, a_arrs)
    b_trains = count_trains(b_deps, b_arrs)
    print 'Case #%d: %d %d' % (case_num+1, a_trains, b_trains)

def main(input):
    f = file(input)
    n = read_int_line(f)
    for i in range(n):
        do_test_case(f, i)
    f.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage: %s <input>' % sys.argv[0]
        sys.exit(1)
    main(sys.argv[1])
