from sys import argv

lines = []
with open(argv[1], 'r') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

cases = int(lines.pop(0))

results = []

for i in xrange(0, cases):
    vals = lines[i].split(' ')
    n = int(vals[0])
    k = int(vals[1])
    
    switches = [0 for x in xrange(0, n)]

    for j in xrange(0, k):
        if switches[0] == 1:
            l = 1
            while l < (n - 1) and switches[l] == 1:
                switches[l] = 0
                l += 1

            if l < n:
                switches[l] = 1 if switches[l] == 0 else 0
            switches[0] = 0
        else:
            switches[0] = 1

    
    result = "ON" if n == len(filter(lambda x: x == 1, switches)) else "OFF"

    results.append('Case #%d: %s' % (i + 1, result))

print "\n".join(results)
