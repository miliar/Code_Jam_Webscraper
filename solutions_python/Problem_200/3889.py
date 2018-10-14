t=input()

for i in range(t):
    N=input()

    repeat=N
    for x in range(repeat):
        n=list(str(N))
        if all(earlier <= later for earlier, later in zip(n, n[1:])):
            print "Case #"+str(i+1)+": "+"".join(n)
            break
        else:
            N-=1