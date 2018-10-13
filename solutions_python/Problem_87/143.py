#!/usr/bin/python

fh = open("A-large.in.txt","r")
lines = fh.readlines()
fh.close()

cases = []
T = int(lines[0].strip())
line_i = 0
for i in range(T):
    line_i +=1
    [L,S, R, t, N] = map(int, lines[line_i].strip().split())
    #print [L,S, R, t, N] 
    walks = []
    for n in range(N):
        line_i +=1
        [B, E, s] = map(int, lines[line_i].strip().split())
        walks += [[B, E, s]]
    cases += [[L,S, R, t, N, walks]]

#print cases

for i in range(len(cases))[:]:
    case = cases[i]
    d={}
    pos1 = 0
    [L,S, R, t, N, walks] = case
    walks1 = []
    for walk in walks:
        [B, E, s] = walk
        if pos1 == B:
            if s not in d:
                d[s]=[]
            d[s]+=[E-B]
            pos1 = E
        else:
            if 0 not in d:
                d[0]=[]
            d[0]+=[B-pos1]
            if s not in d:
                d[s]=[]
            d[s]+=[E-B]
            pos1 = E
    if pos1 != L:
        if 0 not in d:
            d[0]=[]
        d[0]+=[L-pos1]
    #print d
    tot= 0.0
    running = t
    speeds = d.keys()
    speeds.sort()
    #print d, speeds
    for speed in speeds:
        for d1 in d[speed]:
            [speedf, Rf, Sf, d1f] = map(float, [speed, R, S, d1])
            if running >0.0:
                prop_t = d1f/(speedf+Rf)
                if prop_t <= running:
                    tot += prop_t
                    running -= prop_t
                else:
                    #print tot
                    tot += running
                    #print tot, d1, speed, R, S
                    tot += (d1f - running*(speedf+Rf))/(speedf+Sf)
                    #print tot
                    running = -1
            else:
                tot += d1f/(speedf+Sf)
            #print speed, d1, tot, running
    print "Case #"+str(i+1)+": "+str(tot)
