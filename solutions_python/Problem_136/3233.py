import math

def get_n(c,f,x):
    n = math.ceil(x/c-2/f-1)
    if (n<0):
        n = 0;
    return n

def check(c,f,x):
    time = 0;
    n = int(get_n(c,f,x))
    for i in xrange(0, n):
        time+= c/(2+i*f)

    time+=x/(2+n*f)
    return time
        
# Main
t = int(raw_input())

for i in xrange(0,t):
    c, f, x = raw_input().split()
    c = float(c)
    f = float(f)
    x = float(x)
    print "Case #%d:" % (i+1), 
    print("%.7f" % check(c,f,x))
  
