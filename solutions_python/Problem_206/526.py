
def get_speed(d, n, horses):
    horses.sort(key = lambda x: x[0], reverse=True)
    v = horses[0][1]
    tm = (d - horses[0][0]) / v
    
    for i in range(1, n):
        if horses[i][1] <= v:
            v = horses[i][1]
            tm = (d - horses[i][0]) / v
        else:
            x = (horses[i-1][0]*horses[i][1] - horses[i][0]*v) / (horses[i][1] - v)
            if x < d:
                tm = ((x - horses[i][0]) / horses[i][1]) + ((d - x) / v)
                v = (d - horses[i][0]) / tm
            else:
                v = horses[i][1]
                tm = (d - horses[i][0]) / horses[i][1]
    return d / tm
    
    
    
t = int(raw_input())
for i in xrange(1, t + 1):
    line = raw_input()
    (d, n) = map(lambda x: int(x), line.split(' '))
    horses = []
    for j in range(n):
        line = raw_input()
        horses.append(map(lambda x: float(x), line.split(' ')))
    
    print "Case #{}: {}".format(i, get_speed(d, n, horses))
