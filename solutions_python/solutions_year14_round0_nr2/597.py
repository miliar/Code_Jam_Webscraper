import math

f = open('B-large.in', 'r')
g = open('Output.txt', 'w')
T = [int(s) for s in f.readline().split() if s.isdigit()][0]

for i in range (0,T):

    actual_line = [float(s) for s in f.readline().split()]
    C = actual_line[0]
    F = actual_line[1]
    X = actual_line[2]

    print(C,F,X)

    n = max(math.ceil(X/C - 2/F - 1),0)
    print (n)

    if (n == 0):
        t = X/2
    else:
        t = X/(2+n*F)
        for k in range(0,n):
            t = t+C/(2+k*F)     
        
    out_t = '%.7f' % t   

    ans_str = 'Case #'+str(i+1)+': '+out_t
    print(ans_str)
    g.write(ans_str)
    if (i+1 != T):
        g.write('\n')

g.close()
