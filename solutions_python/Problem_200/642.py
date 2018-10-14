T = int(input().strip())
for i in range(T):
    n = list(input().strip())
    post = 0
    ans = ''.join(n)
    if len(n) > 1:
        for j in range(1,len(n)):
            if n[j] > n[j-1]:
                post = j
            elif n[j] < n[j-1]:
                ans = None
                break
        if ans is None:
            n[(post+1):] = ['9']*(len(n)-post-1)
            n[post] = str(int(n[post])-1)
            if n[0] == '0': n[0] = ''
            ans = ''.join(n)
    print("Case #{}: {}".format(i+1,ans))
