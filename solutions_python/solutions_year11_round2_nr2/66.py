import sys

t = int(sys.stdin.readline())

case = 1

while True:
    line = sys.stdin.readline()
    line = line.rstrip()
    if len(line) == 0:
        break

    words = line.split()
    c = int(words[0])
    d = float(words[1])
    #print("c: {} d: {}".format(c,d))

    points = []
    for i in range(c):
        line = sys.stdin.readline()
        words = line.split()
        p = int(words[0])
        v = int(words[1])
        points.append((p,v))
    points.sort()


    m = []
    for j in range(len(points)): # start point
        m.append((points[j][1]-1)*d/2)

    maxd = 0
    combine = 0
    curm = 0
    for i in range(1,c):
        if combine == 0:
            curm = m[i-1]
        if abs(points[i][0] - points[i-1][0]) >= (m[i]+curm+d):
            if max(m[i-1], m[i]) > maxd:
                maxd = max(m[i-1], m[i])
            combine = 0
        else:
            combine += 1
            curcenter = float(abs(points[i-combine][0]-points[i][0]))/2+points[i-combine][0]
            #print("center: {}".format(curcenter))
            vsum = 0
            for k in range(i-combine, i+1):
                vsum += points[k][1]
            #print(vsum)
            curm = (vsum-1)*d/2-(points[i][0]-curcenter)
            curp = curcenter-(vsum-1)*d/2
            for k in range(i-combine, i+1):
                #print("curp: {}, points[k][0]: {}".format(curp, points[k][0]))
                if abs(points[k][0]-curp) > maxd:
                    maxd = abs(points[k][0]-curp)
                curp += (points[k][1])*d

    if c == 1:
        maxd = (points[0][1]-1)*d/2



    print("Case #{}: {}".format(case, maxd))
    case += 1
                
            

