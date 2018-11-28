def lastTidy(N):
    N = list(N)
    for i in range(len(N)-1, 0, -1):
        if N[i] < N[i-1]:
            N[i] = '9';
            for j in range(i, len(N)):
                N[j] = '9';
            N[i-1] = str(int(N[i-1])-1);
    return int("".join(N));

T = input();

for t in range(1, T+1):
    N = raw_input();
    res = lastTidy(N);
    print "Case #"+str(t)+": "+str(res);

