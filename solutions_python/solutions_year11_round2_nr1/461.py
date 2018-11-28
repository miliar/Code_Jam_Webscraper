import sys

def calcWP(data):
    count1 = data.count("1")
    count0 = data.count("0")
    return float(count1) / (count1 + count0)
        
def calcWPs(data):
    WPs = []
    for d in data:
        WPs.append(calcWP(d))
    return WPs

def calcOWP(data, n): # you are n^st team
    OWP = 0.0
    amount = 0
    for i, d in enumerate(data):
        if data[n][i] == ".":
            pass
            continue
        count1 = d.count("1") - [0, 1][d[n] == "1"]
        count0 = d.count("0") - [0, 1][d[n] == "0"]
        OWP += float(count1) / (count1 + count0)
        amount += 1
    
    return OWP / amount

def calcOWPs(data):
    OWPs = []
    for i in range(len(data)):
        OWPs.append(calcOWP(data, i))
    return OWPs

def calcOOWP(data, n): # you are n^st team
    global OWPs
    OOWP = 0.0
    amount = 0
    for i, c in enumerate(data):
        if i == n:
            pass
            continue
        if c == "1" or c == "0":
            OOWP += OWPs[i]
            amount += 1
    return OOWP / amount

def calcOOWPs(data):
    OOWPs = []
    for i, d in enumerate(data):
        OOWPs.append(calcOOWP(d, i))
    return OOWPs


if __name__ == "__main__":
    if len(sys.argv) == 2:
        f = open(sys.argv[1], "r")
        T = int(f.readline().strip())
        for _t in range(T):
            data = []
            N = int(f.readline().strip())
            for _n in range(N):
                d = f.readline().strip()
                data.append(d)
            
            #print data

            WPs = calcWPs(data)
            #print "WPs: " + str(WPs)

            OWPs = calcOWPs(data)
            #print "OWPs: " + str(OWPs)

            OOWPs = calcOOWPs(data)
            #print "OOWPs: " + str(OOWPs)
            
            print "Case #%d:" %(_t + 1)
            for i in range(N):
                print 0.25 * WPs[i] + 0.5 * OWPs[i] + 0.25 * OOWPs[i]
        f.close()
