#!/usr/bin/python

import sys

def process(t, na, nb, tripsa, tripsb):
    tripsa.sort()
    tripsb.sort()
    trainsa, trainsb = [], []
    sizea, sizeb = 0, 0 
    while(tripsa != [] or tripsb != []):
        trainsa.sort()
        trainsb.sort() 
        try:
            ta = tripsa[0]
        except:
            ta = None
        try:
            tb = tripsb[0]
        except:
            tb = None 
        if ta == None:
            first = tb
        elif tb == None:
            first = ta
        else:
            first = min(ta, tb)
        if first == ta:
            curr = "a"
            tripsa = tripsa[1:]
        else:
            curr = "b"
            tripsb = tripsb[1:]
        if curr == "a":
            if trainsa != [] and first[0] >= trainsa[0]:
                trainsa = trainsa[1:]
                trainsb.append(first[1] + t)
            else:
                trainsb.append(first[1] + t)
                sizea += 1
        else:
            if trainsb != [] and first[0] >= trainsb[0]:
                trainsb = trainsb[1:]
                trainsa.append(first[1] + t)
            else:
                trainsa.append(first[1] + t)
                sizeb += 1
    return "%d %d" % (sizea, sizeb)


def g(time):
    hours, mins = map(int, time.split(":"))
    return hours*60 + mins


def main():
    args = sys.argv[1:]
    f = args[0]
    args = open(f).read().split("\n")
    n, args = int(args[0]), args[1:]
    tot = n
    while n > 0:
        tripsa, tripsb = [], []
        t, args = int(args[0]), args[1:]
        (na, nb), args = map(int, args[0].split(" ")), args[1:]
        while na > 0:
            line, args = args[0], args[1:]
            depart, arriv = (line.split(" "))
            tripsa.append( ( g(depart), g(arriv) ))  
            na -= 1
        while nb > 0:
            line, args = args[0], args[1:]
            depart, arriv = (line.split(" "))
            tripsb.append( (g(depart), g(arriv)) )  
            nb -= 1
        tripsa.sort()
        tripsb.sort()
        ans = process(t, na, nb, tripsa, tripsb)
        print "Case #%d: %s" % (tot-n+1, ans)
        n -= 1

if __name__ == "__main__":
    sys.exit(main())
