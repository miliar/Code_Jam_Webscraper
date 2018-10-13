def solve(n):
    ans = [''] * len(n)
    pd = '9'

    for i in range(len(n)-1, -1, -1):
        cd = n[i]
        if cd > pd:
            for j in range(i+1, len(n)):
                ans[j] = '9'
            cd = chr(ord(cd) - 1)
        ans[i] = cd
        pd = cd
    
    return int(''.join(ans))

t = int(input())
for i in range(t):
    print("Case #{0}: {1}".format(i+1, solve(input())))