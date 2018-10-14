from collections import deque

inp = open('C-small-attempt0.in', 'r+')
out = open('output', 'r+')

t = int(inp.readline()) # number of test cases

for i in range(t):
    ints = inp.readline().split(" ")
    a = int(ints[0])
    b = int(ints[1])
    d = len(ints[0]) # number of digits per number
    
    counts = {}
    rotations = {}
    count = 0
    
    for n in range(a, b+1):
        n_str = str(n)
        if n_str in counts:
            count += counts[n_str]
            for rot in rotations[n_str]:
                counts[rot] += 1
        else:
            q = deque(n_str)
            rots = []
            for j in range(d):
                q.rotate()
                next = "".join(q)
                counts[next] = 1
                rots.append(next)
            rots = set(rots)
            for k in rots:
                rotations[k] = rots
    out.write("Case #" + str(i+1) + ": " + str(count) + "\n")
