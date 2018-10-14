#!python
from optparse import OptionParser
from collections import deque
usage = "usage: %prog input"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()
if not args:
	parser.error("input omitted")
f = open(args[0])
T = int(f.readline())

for i in range(1,T+1):
    freesince = dict(O=0,B=0)
    position = dict(O=1,B=1)
    line = deque(f.readline().split())
    N = int(line.popleft())
    
    clock=0
    
    while line:
        bot, target = line.popleft(), int(line.popleft())
        d = abs(target-position[bot])
        
        # move
        clock += max(0, d - (clock - freesince[bot]) )
        position[bot] = target

        # push button
        clock += 1
        freesince[bot] = clock
        

    
    print "Case #%d: %s" % (i,clock)
