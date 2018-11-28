    
import sys

T = int(sys.stdin.readline())
for case in xrange(1, T+1):
    a = int(sys.stdin.readline())
    arra = []
    for _ in xrange(4):
        arra.append(sys.stdin.readline().split())
    
    b = int(sys.stdin.readline())
    arrb = []
    for _ in xrange(4):
        arrb.append(sys.stdin.readline().split())
    
    #print "arra"
    #print arra
    #print "arrb"
    #print arrb
    
    res = set(arra[a-1]) & set(arrb[b-1])
    out = "Case #"+str(case)+": "
    if len(res) == 1:
        out += str(res.pop())
    elif len(res) == 0:
        out += "Volunteer cheated!"
    else:
        out += "Bad magician!"
    print out
