import sys

import psyco; psyco.full()

def subtask(n, events, eventkeys, start, end):
    newcost = 0
    
    while True:
        while events[eventkeys[start]] == 0 and start < end:
            start += 1
            
        while events[eventkeys[end]] == 0 and end >= 0:
            end -= 1
            
        if start >= end:
            return newcost
            
        minpass = 9999999999999999999999999999999999
        ps = 0
        tstart = start
        tend = end
        for i in xrange(start, end):
            ps += events[eventkeys[i]]
            if ps == 0:
                tend = i
                break
        
            minpass = min(minpass, ps)

        # print minpass
        # print events
        # print
        events[eventkeys[tstart]] -= minpass
        events[eventkeys[tend]] += minpass
        # print "dsddsds", events[eventkeys[start]]
        # print "dsddsds", events[eventkeys[end]]
        
        dist = eventkeys[tend] - eventkeys[tstart]
        newcost += minpass * (n * dist - (((dist-1)*dist)/2)) 
            
def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline())
    for caseno in xrange(ncases):
        n, m = f.readline().split()
        n = int(n)
        m = int(m)
        
        basecost = 0
        events = {}
        for i in xrange(m):
            o, e, p = f.readline().split()
            o, e, p = int(o), int(e), int(p)
            dist = e - o
            basecost += p * (n * dist - (((dist-1)*dist)/2))
            if o not in events:
                events[o] = p
            else:
                events[o] += p
            
            if e not in events:
                events[e] = -p
            else:
                events[e] -= p
            
        eventkeys = sorted(events.keys())
        
        newcost = subtask(n, events, eventkeys, 0, len(eventkeys)-1)
            
        print "Case #%d: %d" % (caseno+1, (basecost - newcost) % 1000002013)
        #exit()
main()