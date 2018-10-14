''' 
4
1 9
10 40
100 500
1111 2222

Case #1: 0
Case #2: 3
Case #3: 156
Case #4: 287

'''
from sys import stdin

val = int(stdin.readline())

for i in range(1,val+1):
    a,b = stdin.readline().split()
    recycled = 0
    
    for n in range(int(a),int(b)):
        x = str(n)
        found = [] # To catch duplicates
        for shift in range(1,len(x)):
            y = x[shift:]+x[:shift]
            if n < int(y) <= int(b) and y not in found:
                recycled += 1
                found.append(y)
 
    print 'Case #%s: %s' % (i, recycled)