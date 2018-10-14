f = open('B-large.in', 'r')
o = open('output', 'w')
t = int(f.readline().rstrip())
for i in range(1,t+1):
    R = 2.0
    params = f.readline().rstrip().split()
    C = float(params[0])
    F = float(params[1])
    X = float(params[2])
    time = X/R
    farmtime = C/R
    R = R + F
    newtime = farmtime + X/R
    while newtime < time:
        time = newtime
        farmtime = farmtime + C/R
        R = R + F
        newtime = farmtime + X/R
    o.write('Case #' + str(i) + ': ' + str(time) + '\n')
