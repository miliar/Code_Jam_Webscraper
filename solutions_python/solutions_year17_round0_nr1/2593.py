def solve(s,k):
    n = 0
    while True:
        try:
            first_minus = s.index('-')
        except:
            first_minus = len(s)
        s = s[first_minus:]
        if s == []:
            return n
        if len(s) < k and len(s) > 0:
            return None
        else:
            for i in range(len(s)):
                if i < k:
                    s[i] = '-' if s[i] == '+' else '+'
            n += 1

T = int(input())
for i in range(1,T+1):
    s, k = input().split(' ')
    k = int(k)
    s = list(s)
    res = solve(s,k)
    if res == None:
        print("Case #"+str(i)+": "+"IMPOSSIBLE")
    else:
        print("Case #"+str(i)+": "+str(res))
