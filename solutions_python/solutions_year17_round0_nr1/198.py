for T in range(int(input())):
    s, k = input().split()
    k = int(k)
    s = [(1 if c == "+" else 0) for c in s]
    flip = 0
    for i in range(len(s)-k+1):
        if s[i] == 0:
            for j in range(i,i+k):
                s[j] = 1-s[j]
            flip+= 1
    if all(s):
        res = flip
    else:
        res = "IMPOSSIBLE"
    print("Case #%d: %s"%(T+1,res))