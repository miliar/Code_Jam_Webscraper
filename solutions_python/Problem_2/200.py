import sys
import fileinput

def solve(T, AB, BA):
    A_departs = getStarts(AB) 
    B_departs = getStarts(BA)

    A_arrives = sorted(map(lambda x: x[1] + T, BA))
    B_arrives = sorted(map(lambda x: x[1] + T, AB))

#    print "A"
    solveStation(A_departs, A_arrives)

#    print "B"
    solveStation(B_departs, B_arrives)

    return (sum(A_departs.values()), sum(B_departs.values()))

def solveStation(departs, arrives):
#    print "departs"
#    print departs
#    print "arrives"
#    print arrives
    for start in sorted(departs.items()):
        while len(arrives) > 0 and arrives[0] <= start[0] and departs[start[0]] > 0:
#            print "HI %d" % (arrives[0])
            departs[start[0]] -= 1 
            arrives = arrives[1:]

        if len(arrives) == 0:
            break


def getStarts(schedule):
    m = {}
    for x in schedule:
        if m.has_key(x[0]):
            m[x[0]] += 1
        else:
            m[x[0]] = 1
    return m

def parseTime(str):
    (h, m) = map(int, str.split(':'))
    return h*60 + m

def getTrips(lines, n):
    trips = []
    for i in range(0, n):
        trips.append(map(parseTime, lines.readline().split(' ')))
    return trips

if __name__ == '__main__':
    lines = fileinput.input(sys.argv[1])
    N = int(lines.readline())
    for i in range(1, N+1):
        T = int(lines.readline())
        (NA, NB) = map(int, lines.readline().split(' '))
        AB = getTrips(lines, NA)
        BA = getTrips(lines, NB)

        out = solve(T, AB, BA)
        
        print "Case #%d: %d %d" % (i, out[0], out[1])
