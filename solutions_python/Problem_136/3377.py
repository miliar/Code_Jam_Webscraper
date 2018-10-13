for t in range(int(input())):
    (C, F, X)=([float(x) for x  in input().split()])
    old=tmp=X/2; n=0;
    while tmp - old <= 0:
        n=n+1;old=tmp;
        tmp=X/(2+n*F)+sum([C/(2+x*F) for x in range(n)])
    print('Case #%d: %.7f'%(t+1,old))
