def main ():
    
    input = open("input.txt")
    testcases = int(input.readline())
    
    for case in range(1, testcases+1):
        
        line = input.readline().strip().split()
        if line == "": break
        points = int(line[0])
        mindist = int(line[1])
        
        vendors = []
        for i in range(points):
            line = input.readline().strip().split()
            p = int(line[0])
            v = int(line[1])
            vendors += [p] * v
        vendors.sort()
        dists = [(vendors[i+1] - vendors[i]) for i in range(len(vendors)-1)]
        
        if   len(dists) == 0: time = 0.0
        elif len(dists) == 1: time = float(max(mindist - dists[0], 0))
        else:
            time = 0.0
            while min(dists) < mindist:
                dt = (mindist - min(dists)) / 2.0
                time      += dt
                dists[0]  += dt
                dists[-1] += dt
                for i in range(1, len(dists)):
                    diff = dists[i] - dists[i-1]
                    if abs(diff) > 0:
                        dir = diff / abs(diff)
                        dx = min(dt, abs(diff)) * dir
                        dists[i-1] += dx
                        dists[i]   -= dx
        
        print "Case #%d: %f" % (case, time)


if __name__ == "__main__": main()