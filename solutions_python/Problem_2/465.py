import sys
from itertools import chain, repeat


def getln():
    return sys.stdin.readline().strip()



class Station(object):
    def __init__(self):
        self.arrive = []
        self.depart = []
    def _t_to_int(self, time_str):
        return int(''.join(time_str.split(':')))
    def add_arrival(self, time_str, offset):
        self.arrive.append(self._t_to_int(time_str) + offset)
    def add_departure(self, time_str):
        self.depart.append(self._t_to_int(time_str))
    def sort_times(self):
        self.arrive.sort()
        self.depart.sort()
    def __repr__(self):
        times = zip(chain(self.arrive, repeat(-1)), self.depart)
        return 'Arr\tDep\n' + ''.join("%d\t%d\n"%(a,d) for (a,d) in times)


n_cases = int(getln())

for case in range(1, n_cases+1):
    A, B = Station(), Station()
    
    T = int(getln())
    
    (n_read_atob, n_read_btoa) = (int(tok) for tok in getln().split())
    
    for i in xrange(n_read_atob):
        (t_l, t_r) = getln().split()
        A.add_departure(t_l)
        B.add_arrival(t_r, T)
    for i in xrange(n_read_btoa):
        (t_l, t_r) = getln().split()
        B.add_departure(t_l)
        A.add_arrival(t_r, T)

    A.sort_times()
    B.sort_times()

    #print A
    #print B


    train_counts = [0, 0]
    for (stn, num) in ((A, 0), (B, 1)):
        for i in xrange(len(stn.depart)):
            if stn.arrive and stn.depart[i] >= stn.arrive[0]:
                stn.arrive = stn.arrive[1:]
            else:
                train_counts[num] += 1

    
    print "Case #%d:"%case, train_counts[0], train_counts[1]
    
