import math
def serve(n,p,r,q):
    s = 0
    for i in range(n):
        low = r[i] * 0.9
        up = r[i] * 1.1
        for j in range(p):
            sl = math.ceil(q[i][j] / up)
            su = math.floor(q[i][j] / low)
            q[i][j] = (sl,su)
        q[i].sort()
    
    while(p > 0):
        maxomin = q[0][-1][0]
        for i in range(n):
            if q[i][-1][0] > maxomin:
                maxomin = q[i][-1][0]
        st = 0
        for i in range(n):
            if q[i][-1][1] < maxomin:
                st = 1
                break
        else:
            for i in range(n):
                del q[i][-1]
            s += 1
        if(st):
            for i in range(n):
                if q[i][-1][0] == maxomin:
                    del q[i][-1]
        p -= 1
    return s

        

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n,p = [int(s) for s in input().split(" ")]
    r = [int(s) for s in input().split(" ")]
    q = []
    for j in range(n):
        q.append([int(s) for s in input().split(" ")])
    
    res = serve(n,p,r,q)
    print("Case #{}: {}".format(i, res))