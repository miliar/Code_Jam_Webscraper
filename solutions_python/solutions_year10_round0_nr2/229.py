import sys

list = [];  
pos = 0; 

def read_all() : 
    for line in sys.stdin : 
        list.extend(map(int, line.split(" ")))

def get_int() :      
    global pos     
    res = list[pos]; 
    pos = pos + 1
    return res

def gcd(a,b): 
    if (a > 0): 
        return gcd(b % a, a)
    return b

def abs(a) : 
    if (a < 0) : return -a
    return a;                  
        
read_all(); 
C = get_int(); 
tc = 0 

while (C > 0) : 
    C = C - 1
    N = get_int(); 
    res = 0 
    tl = [] 
    for i in xrange(N):
        tl.append(get_int())
    for i in xrange(1,N):
        res = gcd(res, abs(tl[i] - tl[0]))
    tc += 1        
    res = ((tl[0] + res - 1) / res) * res - tl[0]
    print 'Case #' + str(tc) + ': '+str(res)
