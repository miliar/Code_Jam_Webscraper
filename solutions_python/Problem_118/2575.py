import sys
from Queue import Queue
import math
import re

def _process_fair_square(q, count):
    start = q[0]
    end = q[1]
    i = int(start)
    match_cnt = 0
    while i <= int(end):
        if str(i) == str(i)[::-1]:
            if int(math.sqrt(int(i)))**2 == int( i ):
                if str(int(math.sqrt(int(i)))) == \
                        str( int(math.sqrt(int(i))))[::-1]: 
                    match_cnt = match_cnt + 1
        i = i + 1
    print "Case #%s: %s"%(count, match_cnt)


if __name__ == '__main__':
    try:
        testcases = int(raw_input() )
    except:
        print "Enter a valid input number."
        sys.exit(1)
    cnt = 0
    Q = Queue()
    while cnt < testcases:
        temp = []
        pat = "[0-9]"
        two = raw_input()
        nums = two.split()
        s = nums[0]
        e = nums[1]
        s=int(s)
        e=int(e)
        temp.append(str(s) )
        temp.append(str(e) )
        Q.put( temp )
        cnt = cnt + 1
    
    count = 0
    while Q.qsize() > 0:
        q = Q.get()
        count = count + 1
        _process_fair_square(q, count)

        
