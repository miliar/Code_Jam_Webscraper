# python a.py<sample.txt
import sys
import re
(l,d,n) = sys.stdin.readline().split()
##print l,d,n
lines = sys.stdin.readlines()
data = [x.strip() for x in lines[0:int(d)]]
pattern = [x.strip() for x in lines[int(d):]]

##print 'data'
##print data
##print 'pattern'
##print pattern

for x,p in enumerate(pattern):
    k = 0 # reset count
    p = p.replace('(', '[').replace(')', ']')
    p = '^' + p + '$'
    for d in data:
        if re.match(p,d):
            k += 1
    print 'Case #%d: %d' %(x + 1,k)
