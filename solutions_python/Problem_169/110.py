infile = file("B-small-attempt3.in")
outfile = file("B-small-attempt3.out", "w+")
t = int(infile.readline())
for i in range(t):
    result = 0
    inline = infile.readline().split()
    n = int(inline[0])
    v = float(inline[1])
    x = float(inline[2])
    water_status = []
    for j in range(n):
        inline = infile.readline().split()
        water_status.append([float(inline[0]), float(inline[1])])
    if n == 1:
        if water_status[0][1] != x:
            result = 'IMPOSSIBLE'
        else:
            result = 1.0 * v / water_status[0][0]
    elif n == 2:
        if water_status[0][1] == water_status[1][1]:
            if water_status[0][1] != x:
                result = 'IMPOSSIBLE'
            else:
                result = 1.0 * v / (water_status[0][0] + water_status[1][0])
        elif water_status[0][1] == x:
            result = 1.0 * v / water_status[0][0]
        elif water_status[1][1] == x:
            result = 1.0 * v / water_status[1][0]
        else:
            v1_v2 = (x - water_status[1][1])/(water_status[0][1] - x)
            # print v1_v2, x - water_status[1][1], water_status[0][1] - x
            if v1_v2 < 0:
                result = 'IMPOSSIBLE'
            else:
                t2 = v / (water_status[1][0] * (1.0 + v1_v2))
                # v2 = t2 * water_status[1][0] #
                t1 = v / (water_status[0][0] * (1.0 + 1 / v1_v2))
                # v1 = t1 * water_status[0][0]
                # print v1, water_status[0][1], v1 * water_status[0][1]
                # print v2, water_status[1][1], v2 * water_status[1][1]
                # print x * v
                result = max(t1, t2)
    else:
        pass
    if result == 'IMPOSSIBLE':
        outfile.write("Case #%d: %s\n" % (i+1, result))
    else:
        outfile.write("Case #%d: %f\n" % (i+1, result))
outfile.close()
infile.close()
