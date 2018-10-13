import sys

IN = 0
OUT = 1

def minutes(t):
    """
    Given a time t in the format HH:MM, convert it to a number of minutes since midnight
    """
    hours, minutes = map(int, t.split(':'))
    return hours*60 + minutes


def trains_needed(t, station):
    trains = 0
    for i in xrange(len(station)):
        if station[i][1] == OUT:
            found_a_train = False
            for j in xrange(i):
                if station[j][1] == IN and station[j][0] <= station[i][0]-t:
                    # Make this train not be useable for further departures,
                    # since it will be used for this departure. This is a fairly
                    # disgusting way of doing this.
                    station[j][1] = OUT
                    found_a_train = True
                    break
            if not found_a_train:
                trains += 1
    return trains

def calculate_trains(t, a_sched, b_sched):
    a = []
    b = []

    for train in a_sched:
        a_time, b_time = map(minutes, train.split(' '))
        a.append([a_time, OUT])
        b.append([b_time, IN])

    for train in b_sched:
        b_time, a_time = map(minutes, train.split(' '))
        b.append([b_time, OUT])
        a.append([a_time, IN])

    a.sort()
    b.sort()

    return trains_needed(t, a), trains_needed(t, b)

def main():
    if len(sys.argv) != 2:
        print "Usage: %s input_file" % sys.argv[0]
        return 1
    
    input_file = open(sys.argv[1])
    num_cases = int(input_file.readline())
    
    for case in xrange(num_cases):
        t = int(input_file.readline())
        na, nb = map(int, input_file.readline().split(' '))
        
        a_sched = []
        for i in xrange(na):
            a_sched.append(input_file.readline())
        
        b_sched = []
        for i in xrange(nb):
            b_sched.append(input_file.readline())
        
        a_trains, b_trains = calculate_trains(t, a_sched, b_sched)
        print "Case #%i: %i %i" % (case+1, a_trains, b_trains)

if __name__ == "__main__":
    sys.exit(main())
