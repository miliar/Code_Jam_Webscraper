
import sys

def st2i(ts):
    s = ts.split(':')
    return int(s[0])*60+int(s[1])

class Trip:
    def __init__(self, side, departure, arrival, turnaround):
        self.side = side
        self.s = departure
        self.e = arrival + turnaround
        self.prev = None
        self.status = (0,0)
    def start(self):
        return self.s
    def end(self):
        return self.e
    
def calTrains(ifp):
    T = int(ifp.readline().strip())
    ns = ifp.readline().strip().split()
    na = int(ns[0])
    nb = int(ns[1])
    
    start = [[],[]]
    allstart = []
    for i in range(na):
        d, a = ifp.readline().strip().split()
        t = Trip(0, st2i(d), st2i(a), T)
        start[0].append(t)
        allstart.append(t)
    for i in range(nb):
        d, a = ifp.readline().strip().split()
        t = Trip(1, st2i(d), st2i(a), T)
        start[1].append(t)
        allstart.append(t)
    allstart.sort(key=Trip.start, reverse=True)
    start[0].sort(key=Trip.start)
    start[1].sort(key=Trip.start)
    status = (0,0)
    for i, t in enumerate(allstart):
        ss = start[1-t.side]
        f = False
        for st in ss:
            if st.start()>=t.end() and st.prev is None:
                f = True
                st.prev = t
                break
        sames = status[t.side]+1
        diffs = status[1-t.side]+ ((f and -1) or 0)
        if t.side==0:
            status = (sames, diffs)
        else:
            status = (diffs, sames)
    return status

def main():
    ifp = open(sys.argv[1])
    ofp = open(sys.argv[2], 'w')
    N = int(ifp.readline().strip())
    for i in range(N):
        na, nb = calTrains(ifp)
        ofp.write("Case #%d: %d %d\n" % (i+1, na, nb))
    ifp.close()
    ofp.close()

def test():
    import cStringIO
    input = '''5
3 2
09:00 12:00
10:00 13:00
11:00 12:30
12:02 15:00
09:00 10:30
2
2 0
09:00 09:01
12:00 12:02'''
    
    ifp = cStringIO.StringIO(input)
    ofp = cStringIO.StringIO()
    for i in range(2):
        na, nb = calTrains(ifp)
        ofp.write("Case #%d: %d %d\n" % (i+1, na, nb))
    print ofp.getvalue()

#test()
main()