USE_PSYCHO = True
USE_PSYCHO = False

if USE_PSYCHO:
    import psyco
    psyco.full()



def solve(filecontent):
    lines = filecontent.splitlines()
    T = int(lines[0])
    out = []
    for tcase in xrange(1,T+1):
        print "tcase is ",tcase
        line1 = lines[tcase].split(" ")
        A1 = int(line1[0])
        A2 = int(line1[1])
        B1 = int(line1[2])
        B2 = int(line1[3])
        
        res = 0

        for A in xrange(A1, A2+1):
            for B in xrange(B1, B2+1):
                a,b = max(A,B), min(A,B)
                seq = []
                while b != 0:
                    seq.append (a/b)
                    a,b = b, a%b
                loser = 0
                for q in seq[::-1]:
                    loser += 1
                    if q > 1:
                        loser = 0
                if loser % 2 == 0:
                    res += 1
                    
                    
        tcaseOut = ("Case #%d: " % (tcase,))
        tcaseOut += "%d" % res
        out.append(tcaseOut)
    return "\n".join(out)

f = file("codejam/C-small-attempt0.in").read()
file("codejam/C-small.out",'w').write(solve(f))
