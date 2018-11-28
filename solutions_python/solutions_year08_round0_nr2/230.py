import sys

def time_to_mins(time_string):
    h, m = time_string.split(':')
    return 60*int(h) + int(m)


def shortage_list(departures, readys):
    # I count the shortage - departures raise it and arrivals lower it
    subs = [(t, 1) for t in departures]
    adds = [(t, -1) for t in readys]
    changes = adds + subs
    changes.sort()
    shortage = 0
    yield shortage
    for c in changes:
        t, d = c
        shortage += d
	yield shortage
    
def get_departures_and_readys(turn_around_time, trips):
    ds = []
    rs = []
    for t in trips:
        departure, arrival = t
        ds.append(departure)
	rs.append(arrival + turn_around_time)
    return ds, rs

def train_count(ta_time, a_trips, b_trips):
    a_departures, b_readys = get_departures_and_readys(ta_time, a_trips)
    b_departures, a_readys = get_departures_and_readys(ta_time, b_trips)
    a_max_shortage = max(shortage_list(a_departures, a_readys))
    b_max_shortage = max(shortage_list(b_departures, b_readys))
    return "%d %d" % (a_max_shortage, b_max_shortage)

def do_one_test_case(file):
    turn_around_time = int(file.readline())
    na, nb = (int(n) for n in file.readline().split())
    a_trips = []
    for _ in xrange(na):
	departure, arrival = (time_to_mins(t) for t in file.readline().split())
        a_trips.append((departure, arrival))
    b_trips = []
    for _ in xrange(nb):
	departure, arrival = (time_to_mins(t) for t in file.readline().split())
        b_trips.append((departure, arrival))

    return train_count(turn_around_time, a_trips, b_trips)

def main(argv):
    f = open(argv[1], 'r')
    cases = int(f.readline())
    output_list = []
    for i in xrange(cases):
        output_list.append('Case #%d: %s\n' % (i+1, do_one_test_case(f)))
    f.close()
    if len(argv) > 2:
        expected_f = open(argv[2], 'r')
        expected_list = expected_f.readlines()
        expected_list = expected_list[0:-1]
        if (output_list == expected_list):
            print 'Everything matched!'
        else:
            print 'Actual: %s' % output_list
            print 'Expected: %s' % expected_list
    else:
        print ''.join(output_list)

def test():
    print 'Usage: scriptname.py infile [outfile]'
    print 'I\'ll run the doctests instead!'
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        test()
    else:
        main(sys.argv)
