import math
def get_buys(c,f,x):
    n = f*x - 2*c - c*f
    n = n/(c*f)
    N = math.ceil(n)
    return int(N)

def get_time(c,f,x,n):
    time = 0.0
    speed = 2.0
    for i in range(n):
        time = time + (c/speed)
        speed += f
    
    #final buy
    time += x / speed
    return time 

T = int(raw_input())
for i in range(T):
    c,f,x = map(float,raw_input().split())
    n = get_buys(c,f,x)
    time = get_time(c,f,x,n)
    print "Case #%s: %.7f" % (str(i+1), time)
