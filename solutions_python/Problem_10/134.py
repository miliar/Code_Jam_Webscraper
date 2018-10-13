import sys
import math

input = open(sys.argv[1])

n = int(input.readline().strip())

for caseNumber in xrange(1, n+1):

    (maxLetsOnKey, keysAvail, letsInAlpha) = [int(x) for x in input.readline().strip().split()]
    freq = [(int(f), let+1) for let, f in enumerate(input.readline().strip().split())]
    
    freq.sort(reverse=True)
    
    #print freq
    
    if maxLetsOnKey*keysAvail < letsInAlpha:
        print 'Case #%s: IMPOSSIBLE' % caseNumber
        continue
    
    numStrokes = 0
    for i, (f, let) in enumerate(freq):
        #print 'For letter', let, 'for freq', f, 'keys per let', (i/keysAvail)
        numStrokes += f * (int(i/keysAvail+1))
    
    print 'Case #%s: %s' % (caseNumber, numStrokes)
        
    
    