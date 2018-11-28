def isTidy(s):
    first = -1
    for i in range(1, len(s)):
        if s[i] < s[i-1]:
            first = i-1
    return first

def solve(s):
    if s[0] == '0':
        s = s[1:]
    tidy = isTidy(s)
    #print(s)
    #print(tidy)
    if tidy == -1:
        res = s
    else:
        if tidy == 0 and s[tidy] == '1':
            res = '9'*(len(s)-1)
        else:
            res = s[:tidy]+str(int(s[tidy])-1)+'9'*len(s[tidy+1:])
            res = solve(res)
    return res

T = int(input())
for t in range(T):
    s = input()
    res = solve(s)
    print("Case #{}: {}".format(t+1, res))
