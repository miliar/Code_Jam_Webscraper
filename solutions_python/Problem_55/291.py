import sys, Queue

def main(fName):
    f = open(fName, "r")
    noOfCases = int(f.readline())
    for i in xrange(noOfCases):
        runs, capacity, people = map(int, f.readline().split())
        q = Queue.Queue(people)
        for group in  map(int, f.readline().split()):
            q.put(group)
        firstGroup = q.get()
        totalRiders = 0
        for j in xrange(runs):
            riders = 0
            riderList = []
            while riders + firstGroup <= capacity:
                riders += firstGroup
                riderList.append(firstGroup)
                if q.empty():
                    firstGroup = 0
                    break
                firstGroup = q.get()
            for r in riderList:
                q.put(r)
            if not firstGroup:
                firstGroup = q.get()
            totalRiders += riders
        print "Case #%d: %d" % (i + 1, totalRiders)

main(sys.argv[1])

    
    