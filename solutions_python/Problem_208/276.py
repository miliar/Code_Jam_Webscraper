def fastest(dists, speeds, ends, speed0, end0):
    if len(dists) == 0:
        return 0
    else:
        if end0 > dists[0]:
            old = fastest(dists[1:], speeds[1:], ends[1:], speed0, end0 - dists[0]) + float(dists[0])/speed0
            new = fastest(dists[1:], speeds[1:], ends[1:], speeds[0], ends[0] - dists[0]) + float(dists[0])/speeds[0]
            return min(old, new) 
        return fastest(dists[1:], speeds[1:], ends[1:], speeds[0], ends[0] - dists[0]) + float(dists[0])/speeds[0]



import sys
sys.setrecursionlimit(10000) 
if __name__ == "__main__":
    lines = open(sys.argv[1]).readlines()[1:]
    count = 1
    i = 0
    while i < len(lines):
        n, q = lines[i].strip().split(' ')
        q = int(q)
        n = int(n)

        
        speeds = []
        ends = []
        
        for horse in range(i+1, i+n+1):
            end, spd = lines[horse].strip().split(' ')
            end = float(end)
            spd = float(spd)
            speeds.append(spd)
            ends.append(end)

        dmat = []
        dists = []
        for horse in range(i+n+1, i+n+n):
            ds = [float(x) for x in lines[horse].strip().split(' ')]
            dmat.append(ds)
            dists.append([x for x in ds if x >= 0][0])

            
        time = fastest(dists, speeds[:-1], ends[:-1], 0, 0)
        
        
        i = i + n + n + q + 1
        print "Case #%d: %f" % (count, time)
        count += 1

        
