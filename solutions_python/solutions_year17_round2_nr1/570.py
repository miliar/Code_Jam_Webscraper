
fout = open('out.txt','w')
with open('in.txt') as f:
    T = int(f.readline())
    for case in range(1,T+1):
        line = f.readline()

        line = line.split()
        d = int(line[0])
        n = int(line[1])

        t = []
        for i in range(n):
            line = f.readline()
            line = line.split()
            s = int(line[0])
            v = float(line[1])
            t.append((d-s)/v)

        ans = d / max(t)
    
        
        str = "Case #%d: %f\n" % (case, ans)
        print str,
        fout.write(str)
fout.close()
