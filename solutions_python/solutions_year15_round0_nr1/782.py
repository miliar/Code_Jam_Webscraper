__author__ = 'knusper'


def readint(ip):
    return int(ip.readline())
def readintlist(ip):
    return list(map(int,ip.readline().split()))
def readintset(ip):
    return set(map(int,ip.readline().split()))
def readfloat(ip):
    return float(ip.readline())
def readfloatlist(input):
    return list(map(float,ip.readline().split()))
def readstring(ip):
    return ip.readline().strip()
def writeanswer(op,x,sol):
    op.write("Case #"+str(x)+": "+str(sol)+"\n")

fn="A-large"

ip = open(fn+".in", 'r')
op = open(fn+".out", "w")

for t in range(1,readint(ip)+1):
    smax,ppl=readstring(ip).split(" ")
    ppl=[int(digit) for digit in ppl]
    friends=0
    standing=0
    for x in range(len(ppl)):
        if standing+friends<x:
            friends+=x-(standing+friends)
        standing+=ppl[x]
    writeanswer(op,t,friends)
    print(friends)

op.close()