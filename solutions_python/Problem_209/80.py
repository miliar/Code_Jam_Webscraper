#maximize pi * (max(r)^2 + 2*sum(r*h))

pi = 3.14159265358979323

fout = open('out.txt','w')
with open('in.txt') as f:
    T = int(f.readline())
    for case in range(1,T+1):
        line = f.readline()

        line = line.split()
        n = int(line[0])
        k = int(line[1])

        pancakes = []
        for i in range(n):
            line = f.readline()
            line = line.split()
            r = int(line[0])
            h = int(line[1])
            pancakes.append((r,h))

        pancakes.sort(key=lambda p: -p[0])
        areas = []
        for i in range(n-k+1):
            subpancakes = pancakes[i:]
            r,h = subpancakes[0]
            area = r**2 + 2*r*h
            subpancakes = subpancakes[1:]
            subpancakes.sort(key = lambda p: -p[0]*p[1])
            for j in range(k-1):
                r,h = subpancakes[j]
                area += 2*r*h
            area *= pi
            areas.append(area)
        
        ans = max(areas)
        
        str = "Case #%d: %f\n" % (case, ans)
        print str,
        fout.write(str)
fout.close()
