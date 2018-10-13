def test_case(wires): #for big dataset
    if len(wires) > 1:
        intersections = 0
        
        for i in xrange(1, len(wires)):
            if (wires[0][0] > wires[i][0] and wires[0][1] < wires[i][1]) or \
                    ((wires[0][0] < wires[i][0] and wires[0][1] > wires[i][1])):
                intersections += 1
        wires1 = wires
        wires1.remove(wires1[0])
        
        return intersections + test_case(wires1)
    else: return 0
import sys

sys.setrecursionlimit(1500)

f = open("a.in")
content = f.readlines()

T = int(content[0])
w = open("b.out", "w")

line = 1

for i in xrange(1, T+1):
    N = int(content[line])
    
    wires = []
    
    for k in xrange(line+1, line+N+1):
        ab = content[k].split(" ")
        wires.append( (int(ab[0]), int(ab[1])) )
    
    w.write("Case #%d: %d\n" % (i, test_case(wires)))
    
    line += N + 1
        
w.close()
    
    