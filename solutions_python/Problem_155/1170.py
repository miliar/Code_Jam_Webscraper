T = int(raw_input())

for t in range(T):
    res = 0;
    c = 0;
    line = raw_input()
    smax, s = line.split()
    smax = int(smax)
    
    for i in range(len(s)):
        si = int(s[i])
        c += si
        while(i >= c):
            res += 1;
            c += 1

    print("Case #{0}: {1}".format(t+1, res))
