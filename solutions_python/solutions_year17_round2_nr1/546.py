import sys
'''
Time for closest horse to get there.
If next horse takes longer, that is the time to beat.
Horses that go faster will just get caught up, disregard.

'''

if __name__  == '__main__':
    xx = sys.stdin.readline()
    num = 0
    while True:
        line = sys.stdin.readline()
        if not line: break
        num += 1
        (d, n) = line.strip().split()
        d = int(d)
        n = int(n)
        k = []
        s = []
        ks = {} # map position to speed, slower only - ks[k] = s
        
        for i in range(n):
            (ki,si) = sys.stdin.readline().strip().split()
            ki = int(ki)
            si = int(si)
            if ki in ks:
                if si > ks[ki]: continue # already ahve a slower horse there
            ks[ki] = si

        slow_time = 0
        for ki in sorted(ks.keys(),reverse=True):
            si = ks[ki]
            tm = (d-ki)/float(si)
            if tm > slow_time:
                slow_time = tm
            #print ki,ks[ki],tm
        #print slow_time
        #print d/slow_time
        #print

        print 'Case #'+str(num)+': '+ str(d/slow_time)
