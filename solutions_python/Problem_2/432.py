import sys, datetime, time

def mark_duplicates(incoming, outgoing, tatime):
    for i, o in enumerate(outgoing):

        if o is None:
            continue

        for j, p in enumerate(incoming):

            if p is None:
                continue

            if o >= (p + tatime):
                outgoing[i] = None
                incoming[j] = None
                break

def process_trips(case, tatime, trips):
    a_in = [t[1] for t in trips['from_b']]
    a_out = [t[0] for t in trips['from_a']]
    b_in = [t[1] for t in trips['from_a']]
    b_out = [t[0] for t in trips['from_b']]

    a_in.sort()
    a_out.sort()
    b_in.sort()
    b_out.sort()

    mark_duplicates(a_in, a_out, tatime)
    mark_duplicates(b_in, b_out, tatime)

    print "Case #%d: %d %d" % (case, len(filter(None, a_out)), len(filter(None, b_out)))

def str2time(s):
    t = datetime.time(*time.strptime(s, '%H:%M')[3:5])
    d = datetime.datetime.min.date()
    dtime = datetime.datetime.combine(d, t)
    return dtime

def parse_detail(line):
    return tuple(map(str2time, line.split()))

def main():
    f = sys.stdin
    test_cases_n = int(f.readline())

    for i in xrange(test_cases_n):
        turnaround_dt = datetime.timedelta(minutes=int(f.readline()))
        trips_n = map(int, f.readline().split())
        trips = {
            'from_a' : [],
            'from_b' : [],
        }

        for a in xrange(trips_n[0]):
            trips['from_a'].append(parse_detail(f.readline()))
        for b in xrange(trips_n[1]):
            trips['from_b'].append(parse_detail(f.readline()))

        process_trips(i+1, turnaround_dt, trips)

if __name__ == '__main__':
    main()
