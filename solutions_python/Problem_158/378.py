# Small & Large
# X, R, c

# GABRIEL IF
# (R*C) % X == 0
# X <= 6
# X <= 2*min(R,C)
# not (4 2 n or 4 n 2)
# not (6 3 n or 6 n 3)
# ELSE RICHARD

fin = open("smallD2.txt", "r")
fout = open("smallD2.out", "w+")

T = int(fin.readline())

for n in xrange(T):
    X, R, C = [int(x) for x in fin.readline().split()]

    ans = "GABRIEL" if not(R*C)%X and X <= 6 and X <= 2*min(R,C) and not (X==4 and (R==2 or C==2)) and not (X==6 and (R==3 or C==3)) else "RICHARD"

    print X, R, C, "Case #%i: %s" %(n+1, ans)
    fout.write("Case #%i: %s\n" %(n+1, ans))