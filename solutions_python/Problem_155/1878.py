import sys


fi = sys.stdin
t = int(fi.readline())


for _t in range(t):
    	line = fi.readline().split()
    	s = int(line[0])
    	no = line[1]
    
        total = 0
        needed = 0
        for idx,val in enumerate(no):
            val = int(val)
            if ( idx > total  and val > 0):
                needed += idx - total
                total = total + needed

            total += val
            #print "L:::",val,needed,total

	print "Case #%d: %d" % ((_t+1,needed))		

