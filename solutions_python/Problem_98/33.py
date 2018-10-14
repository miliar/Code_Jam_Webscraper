import math
def reflect(i,j,x,y,w,h):
    rtv = []
    if not (i == x):
        rtv.append((i,2-j))
        rtv.append((i,2*h - j))
    else:
        if j < y:
            rtv.append((i,2-j))
        else:
            rtv.append((i,2*h - j))
    if not (j == y):
        rtv.append((2-i,j))
        rtv.append((2*w - i,j))
    else:
        if i < x:
            rtv.append((2-i,j))
        else:
            rtv.append((2*w - i,j))
    return rtv
def angle(m,n,x,y):
    if x == m:
        if n > y:
            return math.pi/2,0
        else:
            return -math.pi/2,0
    if y == n:
        if m > x:
            return 0,0
        else:
            return math.pi,0
    else:
        if m - x > 0 and n - y > 0:
            return math.atan((n-y)*1.0/(m - x)),1
        elif m - x> 0 and n - y< 0:
            return math.atan((n-y)*1.0/(m - x)),3
        elif m - x< 0 and n - y> 0:
            return math.atan((n-y)*1.0/(m - x)),2
        else:
            return math.atan((n-y)*1.0/(m - x)),4
def dist(i,j,x,y):
    return math.sqrt((i-x) ** 2 + (j-y) ** 2)
    
fin = open('D-small-attempt0.in','r')
fout = open('output.out','w')
T = eval(fin.readline())
for i in range(T):
    tmp = fin.readline()
    data = tmp.split()
    h = eval(data[0])
    w = eval(data[1])    
    d = eval(data[2])
    x = 0;
    y = 0;
    for num in range(h):
        str = fin.readline()  
        if(str.find('X') != -1):
            x = str.find('X') + 0.5
            y = num + 0.5
    h -= 1
    w -= 1
    level = [[(2-x,y),(x,2- y),(2*w-x,y),(x,2*h - y)]]
    s = set()
    s.add((x,y))
    for m,n in level[0]:
        if dist(m,n,x,y) <= d:
            s.add((m,n))
    while(True):
        tmp = []
        for m,n in level[-1]:
            for p,q in reflect(m,n,x,y,w,h):
                if dist(p,q,x,y) <= d and not (p,q) in s:
                    tmp.append((p,q))
                    s.add((p,q))
        if len(tmp) == 0:
            break
        else:
            level.append(tmp)
    a = set()
    s.remove((x,y))
    for m,n in list(s):
        t,p = angle(m,n,x,y)
        if not ((t,p) in a):
            a.add((t,p))  
    print >> fout,"Case #%d: %d" %(i+1,len(list(a)))
fin.close()
fout.close()
