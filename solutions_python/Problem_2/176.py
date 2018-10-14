

import sys, datetime


def sortdep(a, b):
    return cmp(a.dep, b.dep)


def sortarr(a, b):
    return cmp(a.arr, b.arr)


class Train(object):
    def __init__(self, dep, arr):
        self.dep = dep
        self.arr = arr
        
    def __repr__(self):
        return "Train(%r, %r)"%(self.dep, self.arr)
        

class Station(object):
    def __init__(self, turn):
        self.trains = []
        self.count = 0
        self.turn = turn

    def arrive(self, train):
        self.trains.append(train)
        self.trains.sort(cmp=sortarr, reverse=True)
        
    def depart(self, dep, arr):
        # check if there's a train ready for departure... 
        for train in self.trains:
            # check if it didn't departed at the same time and if
            # it already arrived
            h, m = train.arr.hour, train.arr.minute
            m += self.turn
            o, p = divmod(m, 60)
            h += o
            m = p
            try:
                turned = datetime.time(h, m)
            except ValueError:
                ndep = datetime.time(dep.hour-1, dep.minute)
                h -= 1
                turned = datetime.time(h, m)
                if train.dep != dep and turned <= ndep:
                    self.trains.remove(train)
                    train.dep = dep
                    train.arr = arr
                    return train
                
                

            
            if train.dep != dep and turned <= dep:
                self.trains.remove(train)
                train.dep = dep
                train.arr = arr
                return train
        else:
            # no train fits us, create a new one
            self.count += 1
            train = Train(dep, arr)
            return train


def main():

    n = int(sys.stdin.readline())

    for c in xrange(n):
        T = int(sys.stdin.readline())
        NA, NB = map(int, sys.stdin.readline().split())

        table = []
        for i in xrange(NA):
            dep, arr = sys.stdin.readline().strip().split()
            dep = datetime.time(*[int(x) for x in dep.split(":")])
            arr = datetime.time(*[int(x) for x in arr.split(":")])
            table.append((0, 1, dep, arr))
        for i in xrange(NB):
            dep, arr = sys.stdin.readline().strip().split()
            dep = datetime.time(*[int(x) for x in dep.split(":")])
            arr = datetime.time(*[int(x) for x in arr.split(":")])
            table.append((1, 0, dep, arr))

        table.sort(key=lambda k: k[2])

        stations = (Station(T), Station(T))

        for src, dest, dep, arr in table:
            train = stations[src].depart(dep, arr)
            stations[dest].arrive(train)


        print "Case #%d: %d %d"%(c+1, stations[0].count, stations[1].count)
        

        
main()

        
