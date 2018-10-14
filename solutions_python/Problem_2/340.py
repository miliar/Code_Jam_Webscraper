class read_in:
    def __init__(self,fn):
        self.it=open(fn)
    def next(self):
        return self.it.next().strip()

def calc_time(d):
    dh,dm = map(int, d.split(":"))
    return dh*60 + dm
    
def get_table(it,N,S):
    dN=[]
    for i in range(N):
        d,a = map( calc_time, it.next().split() )
        dN.append( (d,a, S) )
    return dN
    
class Train:
    def __init__(self, st, t):
        self.station = st
        self.time = t

class Route:
    def __init__(self, dep, arv, st ):
        self.station = st
        self.dep_time = dep
        self.arv_time = arv
        
def find_train(trains, route):
    #print "*", trains, route
    for k in range(len(trains)):
        train = trains[k]
        if train.station == route.station and train.time <= route.dep_time:
            return k
    return -1
        
def run_train(trains,route, tres, T):
    ind = find_train(trains, route)
    if ind == -1:
        trains.append(Train(route.station, route.dep_time))
        tres[route.station]+= 1
    train = trains[ind]
    train.station = 1-train.station #switch
    train.time = route.arv_time + T
    trains.sort( key = lambda t: t.time )


if __name__ == "__main__":
    it = read_in("B-large.in")
    N = int(it.next())
    for n in range(N):
        T = int(it.next())
        NA,NB=map(int, it.next().split() )
        detNA = get_table(it,NA, 0)
        detNB = get_table(it,NB, 1)
        
        D = detNA + detNB
        D.sort()
        R = []
        for t in D:
            r = Route( *t )
            R.append(r)
        
        tres=[0,0]
        trains= []
        
        for route in R:
            run_train(trains,route, tres, T)
                
        print "Case #%d: %d %d" %(n+1,tres[0], tres[1])


