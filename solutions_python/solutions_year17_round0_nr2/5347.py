for _ in range(input()):
    n=raw_input()
    p=int(n)
    while p>=0:
        n=str(p)
        r="".join(sorted(n))
        if n==r:
            print "Case #"+str(_+1)+": "+str(n)
            break
        p=p-1
