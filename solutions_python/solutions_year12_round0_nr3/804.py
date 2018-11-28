import sys
T = int(sys.stdin.readline())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split(' '))
    rv = 0
    boo = set()
    for n in range(A, B+1):
        for m in range(n+1, B+1):
            for p in range(len(str(n))-1):
                sn = str(n)
                sm = str(m)
                if (sn+sm) not in boo and sn[p+1:]+sn[:p+1] == sm:
                    boo.add(sn+sm)
                    #print(sn,sm)
                    rv += 1
    print("Case #%d:" % (i+1), rv)
