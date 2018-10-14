import math
f = open('A-small-attempt0 (1).in', 'r')
g = open('bullseyeoutput.txt', 'w')
n = int(f.readline())
count = 0
for i in range (1, n+1):
    r, t = [int(x) for x in f.readline().split()]
    ringsize = 2*r+1
    while (ringsize < t+1):
    	t =  t - ringsize
    	ringsize = ringsize + 4
    	count = count + 1
    print count
    line = 'Case #' + str(i) + ': ' + str(count) + '\n'
    g.write(line)      
    count = 0
f.close()
g.close()