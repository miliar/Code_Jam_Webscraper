import sys,copy,itertools
with open(sys.argv[1]) as f:
    for x in range(int(f.readline())):
        a = f.readline().strip()
        R = [x for x in list(a)]
        I = R
        if I == sorted(I,reverse = True):
            I = sorted(I)
            I = I[0:1]+["0"]+I[1:]
            nz = 0
            while I[nz] == "0":
                nz += 1
            I[0],I[nz]=I[nz],I[0]
            s = ""
            for c in I: s+= c
            print("Case #",str(x+1),": ",s,sep="")
            continue
        P = [list(x) for x in itertools.permutations(R)]
        end = sorted(I,reverse = True)
        for p in P:
            if p>I:
                end = min(end,p)
                
        s = ""
        for c in end: s+= c
        print("Case #",str(x+1),": ",s,sep="")
