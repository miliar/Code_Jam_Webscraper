import os,sys, itertools


def is_possible(t, posC, posR, negC, negR, exR, V, X):
    exV = exR * t

    if exV >= V:
        return True

    V = V - exV
    posV = 0
    for i in range(len(posC)):
        posV = posV + posR[i] * t
        pos

DOWNLOADS = "C:\\Users\\vasiliy.strelnikov\\Downloads"

sel_files = []
for fname in os.listdir(DOWNLOADS):
	if fname[:2] == "B-" and fname[-3:] == ".in":
		print len(sel_files), ":", fname
		sel_files.append(fname)

ix = int(sys.stdin.readline())

infile  = sel_files[ix]
outfile = infile[:-3] + ".out"

ifile = open(DOWNLOADS + "\\" + infile)
ofile = open(DOWNLOADS + "\\" + outfile, "w")

T = int(ifile.readline().strip())
for t in range(T):
    N, V, X = ifile.readline().strip().split()
    N = int(N)
    V = float(V)
    X = float(X)

    R=[]
    C=[]
    for n in range(N):
        r, c = ifile.readline().strip().split()
        R.append(float(r))
        C.append(float(c))

    #print N, R, C

    R1 = R[0]
    C1 = C[0]

    if N == 1:
        if C1 != X:
            a = "IMPOSSIBLE"
        else:
            a = str(V / R1)
    else:
        R2 = R[1]
        C2 = C[1]

        #print C1, C2, X

        if (C1 == X and C2 != X):
            a = str(V / R1)
        elif (C2 == X and C1 != X):
            a = str(V / R2)
        elif (C1 == X and C2 == X):
            a = str(V / (R1 + R2))
        elif (C1 > X and C2 > X) or (C1 < X and C2 < X):
            a = "IMPOSSIBLE"
        else:
            if C1 < X:
                Cn, Rn = C1, R1
                Cp, Rp = C2, R2
            else:
                Cn, Rn = C2, R2
                Cp, Rp = C1, R1

            D  = Rp*Rn*(Cp-Cn)
            tn = V*Rp*(Cp - X) / D
            tp = V*Rn*(X - Cn) / D
            a = str(max(tp, tn))

    #tmax = 1e6
    #tmin = 0
    #
    #while abs(tmax - tmin) > 1e-6:
    #    tmid = (tmin + tmax) / 2;
    #      
    #    if is_possible(tmid):
    #        tmax = tmid;
    #    else:
    #        tmin = tmid

    ans = "Case #" + str(t+1) + ": " + a
    print ans
    ofile.write(ans + "\n")