inn = open('input.txt', 'r')
def getz():
    global inn
    return inn.readline().strip()

# Convert everything into seconds.
# Add turnaround time to each arrival to consider
# equivalent problem with no turnaround time.

def secondify(x,addit):
    #print x,addit
    [a,b] = x.split()
    a = a.replace(':',' ')
    b = b.replace(':',' ')
    a = map(int,a.split())
    b = map(int,b.split())
    a = a[0]*60 + a[1]
    b = b[0]*60 + b[1]+addit #dirty use of multiple types in python
    #print a,b
    return (a,b)

def process(xlist,ylist,z=0):
    #xlist = list of arrivals, ylist = list of departures
    if len(xlist) == 0:
        # there are no more arrivals.  z += min(rt, len(ylist))
        return z
    if len(ylist) == 0:
        # there are no more departures.
        return z
    if xlist[0] <= ylist[0]:
        # if a train arrives in time for the next departure
        return process(xlist[1:], ylist[1:], z+1)
    if xlist[0] > ylist[0]:
        # if a train hasn't arrived yet when the next one needs to leave
        return process(xlist, ylist[1:], z)
    
    #print xlist,ylist
n = int(getz())
for testcase in range(n):
    m = int(getz())  #turnaround time
    [a,b] = map(int,getz().split())
    aa = []
    bb = []
    for i in range(a):
        aa.append( secondify(getz(), m))
    for i in range(b):
        bb.append( secondify(getz(), m))
    aaONES = map(lambda x: x[0], aa)
    aaTWOS = map(lambda x: x[1], aa)
    bbONES = map(lambda x: x[0], bb)
    bbTWOS = map(lambda x: x[1], bb)
    aaONES.sort()
    aaTWOS.sort()
    bbONES.sort()
    bbTWOS.sort()
    x = process(aaTWOS,bbONES)
    y = process(bbTWOS,aaONES)
    print "%s%d%s %d %d" %('Case #',testcase+1,':',a-y,b-x)
