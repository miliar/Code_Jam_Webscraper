for xyz in range(1,int(input())+1):
    s,k = input().split()
    s = list(s)
    k = int(k)
    n = len(s)
    ans = 0
    for i in range(n-k+1):
        if s[i] == '-':
            ans += 1
            for j in range(i,i+k):
                if s[j] == '-':
                    s[j] = '+'
                else:
                    s[j] = '-'
    if '-' in s:
        print("Case #"+str(xyz)+": IMPOSSIBLE")
    else:
        print("Case #"+str(xyz)+": "+str(ans))