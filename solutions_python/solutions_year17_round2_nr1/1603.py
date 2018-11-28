import sys, StringIO

DEBUG = 0

def solution(d, h):
    h.sort(lambda a,b: a['k']-b['k'])
    if DEBUG: print "d: %d, h: %s" % (d, h)
    h.sort(lambda a,b: a['k']-b['k'])
    t = 0.0
    while len(h)>1:
        #ith horse will reach next horse at x
        if h[0]['s']>h[1]['s']:
            t1 = 1.0*(h[1]['k']-h[0]['k'])/(h[0]['s']-h[1]['s'])
            x = h[0]['s']*t1+h[0]['k']
            if DEBUG: print "Will meet at %s" % x
            #horse0 will reach horse1 after d
            if x>d:
                h.pop(1)
            else:
                #count time up to meet horse1
                t+=1.0*(x-h[0]['k'])/h[0]['s']
                h[1]['k'] = x
                h.pop(0)
        else:
            h.pop(1)
        if DEBUG: print "time left: %f, %s" % (t, h)

    t+=1.0*(d-h[0]['k'])/h[0]['s']
    if DEBUG: print "End time: %f" % t
    return d/t
#solution


if __name__ == '__main__':
    if len(sys.argv)>1:
        input = file(sys.argv[1])
    else:
        input = StringIO.StringIO("""4
2 1
1 10000
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10""")
    cases = int(input.readline())
    for case in range(cases):
        d, n = map(int, input.readline().split())
        h = []
        for x in range(n):
            k, s = [int(x) for x in input.readline().split()]
            h.append( {'k':k, 's':s} )
        print("Case #%d: %1.6f" % (case+1, solution(d, h)))