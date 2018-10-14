def parse_time(time_str):
    tokens = time_str.split(":")
    hr = int(tokens[0])
    min = int(tokens[1])
    return hr * 60 + min

def get_min(p_list):
    min = 0
    sum = 0
    for itm in p_list:
        sum = sum + int(itm[1])
        if sum < min:
            min = sum
    return min

def comp(a, b):
    if a[0] != b[0]:
        return a[0] - b[0]
    return b[1] - a[1]


f = open("c:/users/roy/Downloads/B-large.in")
#f = open("C:/Users/Roy/Documents/gcj/trains/test.in.txt")

nCnt = 0
lines = f.readlines()

nCnt = int(lines[0])
#print "There are %i test cases." % nCnt
nCase = 0

nLineNo = 1
for nCase in range(1, nCnt+1):
    list_a = []
    list_b = []
    #print "Case #%i:" % nCase
    t = int(lines[nLineNo])
    #print "Turn around time: %i" % t
    nLineNo = nLineNo + 1
    line = lines[nLineNo]
    tokens = line.split()
    trips_a = int(tokens[0])
    trips_b = int(tokens[1])
    nLineNo = nLineNo + 1
    #print "Trips from A: %i" % trips_a
    #print "Trips from B: %i" % trips_b
    for nTripA in range (1, trips_a+1):
        line = lines[nLineNo]
        #print "Trip from A to B: %s" % line
        tokens = line.split()
        time_a = parse_time(tokens[0])
        #print "Departure time from A: %i" % time_a
        list_a.append( (time_a, -1) )
        time_b = (parse_time(tokens[1]) + t)
        #print "Arrival time at B: %i" % time_b
        list_b.append( (time_b, 1) )
        nLineNo = nLineNo + 1
    for nTripB in range (1, trips_b+1):
        line = lines[nLineNo]
        #print "Trip from B to A: %s" % line
        tokens = line.split()
        time_b = parse_time(tokens[0])
        #print "Departure time from B: %i" % time_b
        list_b.append( (time_b, -1) )
        time_a = (parse_time(tokens[1]) + t)
        #print "Arrival time at A: %i" % time_a
        list_a.append( (time_a, 1) )
        nLineNo = nLineNo + 1
    list_a = sorted(list_a, comp)
    #print str(list_a)
    min_a = get_min(list_a) * -1
    list_b = sorted(list_b, comp)
    #print str(list_b)
    min_b = get_min(list_b) * -1
    print "Case #%i: %i %i" % (nCase, min_a, min_b)
        
"""
for line in lines[1:]:
    #print "Test case: %s" % line
    nCase = nCase + 1
    print "Case #%i:" % nCase    
    tokens = line.split()
    atl(tokens[0], tokens[1])
    if nCase >= nCnt:
        break """