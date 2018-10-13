import sys
import math

n = int(sys.stdin.readline().strip())

for case in range(0, n):
    string, flipper = sys.stdin.readline().strip().split(" ")
    flipper = int(flipper)
    
    mask = 0
    for x in range(0, flipper):
        mask = (mask<<1)|1
    
    buff = 0
    fill = False
    count = 0
    for i in range(0, len(string)):
        ch = string[i]
        if ch == "+" and not fill:
            continue
            
        if not fill and ch == "-":
            fill = True
        
        buff = buff<<1
        if ch == "-":
            buff = buff|1
            
        if int(math.log(buff, 2)) + 1 == flipper:
            buff = buff^mask
            count += 1
            if buff == 0:
                fill = False
            
    if buff > 0:
        count = 'IMPOSSIBLE'
    
    print "Case #%s: %s" % ((case+1), count)
    