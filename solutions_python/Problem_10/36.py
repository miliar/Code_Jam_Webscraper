import sys, math

def handle(infile, outfile):
    maxpresses, nkeys, nletters = [int(x) for x in infile.readline().split()]
    freq = [int(x) for x in infile.readline().split()]
    
    keys = [[] for i in range(nkeys)]
    curkey = 0
    freq.sort(reverse = True)
    
    i = 0
    while i < len(freq):
        key = freq[i]
        if len(keys[curkey]) < maxpresses:
            keys[curkey].append(key)
            i += 1
        curkey = (curkey + 1) % nkeys
    
    cost = 0
    for presses in keys:
        for i, f in enumerate(presses):
            cost += (i + 1) * f
    
    outfile.write(' %d' % cost)

if len(sys.argv) != 2: exit()
infile = file(sys.argv[1], 'r')
outfile = file(sys.argv[1] + '.out', 'w')

count = int(infile.readline())
for i in range(count):
    print 'Case #%d' % (i + 1)
    outfile.write('Case #%d:' % (i + 1))
    result = handle(infile, outfile)
    outfile.write('\n')
