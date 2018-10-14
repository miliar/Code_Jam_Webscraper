import sys
from dictset import DictSet
from sets import Set

f = sys.stdin
if len(sys.argv) >= 2:
	fn = sys.argv[1]
	if fn != '-':
       		f = open(fn)
        t = int(f.readline())
        for _t in xrange(t):
                s = f.readline().split()
                if len(s[0]) == 1:
                        print "Case #%d: 0"%(_t+1)
                else:
                        pairs = 0
			start = int(s[0])
			end = int(s[1])
		        length = len(str(start))
		        for i in xrange(start,end):
		                num = str(i)
				sett = set()
		                for j in xrange(1,length):
		                        recycled = num[j:]+num[:j]
		                        recycled = int(recycled)
		                        if i < recycled <= end:
						if recycled not in sett:
							sett.add(recycled)
			                                pairs = pairs + 1
                        print "Case #%d: %d"%(_t+1,pairs)

