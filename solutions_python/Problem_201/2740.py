class stall:
    def __init__ (self, index, state):
        self.index = index
        self.state = state
        self.Ls = None
        self.Rs = None
        self.minimum = None
        self.maximum = None
    def setLs(self, Ls):
        self.Ls = Ls
    def setRs(self, Rs):
        self.Rs = Rs
    def setMinMax(self):
        self.minimum = min(self.Ls, self.Rs)
        self.maximum = max(self.Ls, self.Rs)
    def pick(self):
        self.state = 1
        self.Ls = None
        self.Rs = None
        self.minimum = None
        self.maximum = None

def findLs(value):
    for i in value:
        counterLs = 0
        if (i.state == 0):
            j = i.index-1
            while j >= 0:
                if (value[j].state == 1):
                    break
                counterLs += 1
                j -= 1
            i.setLs(counterLs)
    return value

def findRs(value):
    for i in value:
        counterRs = 0
        if (i.state == 0):
            j = i.index+1
            while j < len(value):
                if (value[j].state == 1):
                    break
                counterRs += 1
                j += 1
            i.setRs(counterRs)
    return value


t = int(raw_input())
for i in xrange(1, t + 1):
    n, m = [int(s) for s in raw_input().split(" ")]
    stalls = []
    for j in xrange(n+2):
        if j == 0 or j == n+1:
            stalls.append(stall (j, 1))
        else:
            stalls.append(stall (j, 0))

    #pick stall process start
    for j in xrange(m):
        #look left and right for occupied stalls
        stalls = findLs(stalls)
        stalls = findRs(stalls)
        #count mins and maxs of each stall
        for k in stalls:
            if k.state == 0:
                k.setMinMax()
        #find the stall(s) with the maximal minimum
        minim = max(stalls, key = lambda x: x.minimum).minimum
        stallsMaxiMini= []
        for k in stalls:
            if k.minimum == minim:
                stallsMaxiMini.append(k.index)
        #check how many stalls with maximal minimum
        if len(stallsMaxiMini) > 1:
            #if found multiple, check maximal maximal of those
            temp = []
            for l in xrange(len(stallsMaxiMini)):
                temp.append(stalls[stallsMaxiMini[l]])
            maxim = max(temp, key = lambda x: x.maximum).maximum
            stallsMaxiMaxi = []
            for k in temp:
                if k.maximum == maxim:
                    stallsMaxiMaxi.append(k.index)
            stalls[stallsMaxiMaxi[0]].pick()
        else:
            #if found one, pick it
            maxim = stalls[stallsMaxiMini[0]].maximum
            stalls[stallsMaxiMini[0]].pick()
    #pick stall process end

    print "Case #{}: {} {}".format(i, maxim, minim)
