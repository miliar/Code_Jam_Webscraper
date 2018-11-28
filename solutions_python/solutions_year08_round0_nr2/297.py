TEST = False
FILENAME = "B-large.in"

def toMin(s):
    """ from xx:xx to minutes
    >>> toMin("01:01")
    61
    """
    return int(s[:2]) * 60 + int(s[3:])

def main():
    def p(line):
        print line
        fo.write(line + "\n")

    if TEST:
        fi = file("foo.txt")
    else:
        fi = file("/Users/nishio/Desktop/" + FILENAME)
    fo = file("/Users/nishio/0", "w")

# main code here
    UPPER_BOUND = 10000 
    num_test = int(fi.readline())
    for test_id in range(num_test):

        tatime = int(fi.readline())
        na, nb = map(int, fi.readline().split())
        event_table = []
        # event_table (time, arrive/depart as -1/+1, A/B as 0/1)
        # order and depart==+1 is important to handle synchronous events
        #print "a to b"
        for i in range(na):
            line = fi.readline().split()
            #print line
            dept, arrv = map(toMin, line)
            event_table.append((dept, +1, 0))
            event_table.append((arrv + tatime, -1, 1))

        #print "b to a"
        for i in range(nb):
            line = fi.readline().split()
            #print line
            dept, arrv = map(toMin, line)
            event_table.append((dept, +1, 1))
            event_table.append((arrv + tatime, -1, 0))

        event_table.sort()
        result = [0, 0]
        trains = [0, 0]
        for (t, diff, pos) in event_table:
            #print (t, diff, pos), trains, result
            trains[pos] -= diff
            if trains[pos] < 0:
                trains[pos] += 1
                result[pos] += 1

        p("Case #%d: %d %d" % (test_id + 1, result[0], result[1]))
    
    fi.close()
    fo.close()

#import doctest
#doctest.testmod()
main()

