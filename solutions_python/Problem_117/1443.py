def check(F, n, m):
    for i in range(n):
        for j in range(m):
            if F[i][j] == "1":
                allowH = True
                for k in range(m):
                    if not F[i][k] == "1":
                        allowH = False
                allowV = True
                for k in range(n):
                    if not F[k][j] == "1":
                        allowV = False
                if not (allowH or allowV):
                    print "NO"
                    return


    print "YES"

f = open('B-small-attempt3.in')
T = int(f.readline().strip())
for t in range(T):
    (N,M) = f.readline().split(' ');

    F = []
    for n in range(int(N)):
        F.append(f.readline().strip().split(' '))

    #for n in range(int(N)):
    #    print F[n]
    print "Case #" + str(t + 1) + ":",
    check(F, int(N), int(M))
    #raw_input("A") 
