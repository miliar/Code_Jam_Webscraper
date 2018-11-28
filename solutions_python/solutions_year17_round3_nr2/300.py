for t in range(input()):
    c,j = map(int,raw_input().strip().split())
    ac = []
    aj = []
    for i in range(c):
        ac.append(map(int,raw_input().strip().split()))
    for i in range(j):
        aj.append(map(int,raw_input().strip().split()))
    if not ac:
        if len(aj)==1:
            ans = 2
        elif len(aj)==2:
            aj = sorted(aj, key=lambda x : x[0])
            if (aj[1][1]-aj[0][0])<=720  or (1440+aj[0][1]-aj[1][0])<=720:
                ans = 2
            else:
                ans = 4
    elif not aj:
        if len(ac)==1:
            ans = 2
        elif len(ac)==2:
            ac = sorted(ac, key=lambda x : x[0])
            if (ac[1][1]-ac[0][0])<=720 or (1440+ac[0][1]-ac[1][0])<=720:
                ans = 2
            else:
                ans = 4
    else:
        ans = 2
    print "Case #{}: {}".format(t+1,ans)