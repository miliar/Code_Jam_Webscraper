import math
t = input()
c = 1

while t:
    data = raw_input().split()
    d = float(data.pop(0))
    n, a = [int(i) for i in data]
    
    points = []
    for i in xrange(n):
        points.append([float(i) for i in raw_input().split()])
    
    accs = [float(i) for i in raw_input().split()]
    
    if len(points) == 1:
        points.append([points[0][0]+1, points[0][1]])
    
    if points[1][1] != points[0][1]:
        t1 = (d - points[0][1]) * (points[1][0] - points[0][0]) / (points[1][1] - points[0][1]) + points[0][0]
    else:
        t1 = 0
    
    print 'Case #%d:' % (c,)
    for i in accs:
        t2 = math.sqrt(2 * d / i)
        print round(max(t1, t2), 7)
    
    t -= 1
    c += 1
