import sys
T = int(sys.stdin.readline().strip())
remt = T
while remt > 0:
    # start test case
    N = int(sys.stdin.readline().strip())
    wires = {}
    crossings = 0
    while N > 0:
        (A, B) = (int(i) for i in sys.stdin.readline().strip().split(' '))
        wires[A] = B # build a dictionary of the wire connections
        #print wires
        
        #for wire in arecrossed:
        #    if wire > A:
       #         crossings += 1
        #    else:
       #         arecrossed.remove(wire)
      #  arecrossed.append(B)
        N -= 1
    for wire in wires.keys():
        #print wire
        for otherwire in wires.keys():
            if wire < otherwire and wires[wire] > wires[otherwire]:
                crossings += 1
    print "Case #" + str(T - remt + 1) + ":", crossings
    remt -= 1
