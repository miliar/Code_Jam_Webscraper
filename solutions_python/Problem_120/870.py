#!/usr/bin/python

num = None
problem = []

def paint1(R):
    return 2*R+1

def paint(r,t):
    ml = t
    times = 0
    radious = r
    while True:
        if ml >= paint1(radious):
            ml -= paint1(radious)
            times += 1
            radious += 2
            # print "paint:%d"%ml
            # print "radious:%d"%radious
        else:
            if times is 0:
                print "ERROR?"
                print r,t
            return times

for line in open("./A-small-attempt1.in","r"):
    print line
    if not num:
        num = int(line)
    else:
        problem.append({"r":int(line.split()[0]),"t":int(line.split()[1])})

time = 1
fp = open("output","w")
for prob in problem:
    fp.write("Case #%d: %d\n"%(time,paint(prob["r"],prob["t"])))
    time += 1
