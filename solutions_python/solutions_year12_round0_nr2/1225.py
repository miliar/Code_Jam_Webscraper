import pprint
import codecs
import copy

def getTriplet(t, delta):
    triplet = (0,0,0)
    found = False
    for i in range(10,-1,-1):
        #print "i: " + str(i)
        for j in range(i, -1, -1):
            #print " j: " + str(j)
            if i + j > t or i-j > delta:
                #print ""
                continue
            for k in range(j, -1, -1):
                #print "  k: " + str(k)
                if i-k > delta or j - k > delta: break
                if i + j + k == t:
                    found = True
                    triplet = (i,j,k)
                    break
            if found: break
        if found: break
    print triplet
    return triplet

file = codecs.open("dancing.large.in", encoding="utf-8", mode="r")
outfile = codecs.open("dancing.large.out", encoding="utf-8", mode="w")
totalCases = int(file.readline())
for case in range(totalCases):
    line = file.readline().rstrip('\n').split(' ')
    N = int(line[0])
    S = int(line[1])
    p = int(line[2])
    ts = [int(x) for x in line[3:]]
    print "N: " + str(N) + " " + "S: " + str(S) + " " + "p: " + str(p) + " " + "ts: " + str(ts)
    answer = 0
    for t in ts:
        print "--t: " + str(t)+ "--"
        print "--S: " + str(S)+ "--"
        triplet = getTriplet(t, 1)
        if len([x for x in triplet if x >= p]) > 0:
            answer += 1
        else:
            if S > 0:
                print "Trying again with delta = 2"
                triplet = getTriplet(t, 2)
                if len([x for x in triplet if x >= p]) > 0:
                    S -= 1
                    answer += 1

    print "S: " + str(S)
    print "Case #" + str(case+1) + ": " + str(answer)
    outfile.write("Case #" + str(case+1) + ': ' + str(answer) + '\n')
