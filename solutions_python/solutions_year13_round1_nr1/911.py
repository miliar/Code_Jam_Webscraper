def nr(r,t):
    x = float(19)
    r = float(r)
    t = float(t)
    for doit in range(20000):
        x = x - (f(x,r,t)/g(x,r,t))
    return x

def f(x,r,t):
    return 2*x*x + (2*r-1)*x - t

def g(x,r,t):
    return 4*x + 2*r - 1

with open('input.in') as fi:

    outfile = open('output.out','w')
    
    cases = int(fi.readline())
    for case in range(1,cases+1):
        r,t = [int(a) for a in fi.readline().split(' ')]
        result = nr(r,t)
        print result
        floor = int(result)
        print "Case #%d: %d" % (case,floor)
        outfile.write("Case #%d: %d\n" % (case,floor))
        
