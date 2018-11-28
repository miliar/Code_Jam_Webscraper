import sys

    
num_cases = int(sys.stdin.readline())


def get_ints(n, wires):
    wires.sort()
    wires_copy = list(wires)
    
    y_counts = {}
    while wires_copy:
        x, y = wires_copy.pop(0)
        remaining_ys = [b for a, b in wires_copy]
        count = 0
        for b in remaining_ys:
            if b < y:
                count += 1
        y_counts[y] = count
    
    num_ints = 0
    while wires:
        x, y = wires.pop(0)
        num_ints += y_counts[y]
    
    return num_ints


for j in xrange(num_cases):
    n = int(sys.stdin.readline().strip())
    
    wires = []
    for i in xrange(n):
        x, y = [int(e) for e in sys.stdin.readline().split()]
        wires.append((x, y))
    
    print "Case #%s: %s" % (j+1, get_ints(n, wires))
    j += 1
