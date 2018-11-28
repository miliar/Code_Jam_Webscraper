f = [l[:-1] for l in file("in")]
cases = int(f[0])

f=f[1:]

case=0
for x in range(cases):
    case+=1
    num_wires = int(f[0])
    f = f[1:]
    wires = []
    for x in range(num_wires):
        wires.append([int(x) for x in (f[0].split(" "))])
        f = f[1:]
    
    intersections=0
    for i,elem in enumerate(wires):    
        for y in wires[:i]:
            if (elem[0] > y[0] and elem[1] > y[1]) or (elem[0] < y[0] and elem[1] < y[1]):
                continue
            intersections+=1
    print "Case #%d: %d" % (case, intersections)
