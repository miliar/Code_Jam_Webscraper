def solve(s):
    ind = -1
    for i in range(1,len(s)):
        if s[i] < s[i-1]:
            ind = i
            break
    if ind == -1: return "".join(map(str,s))
    for i in range(ind+1,len(s)):
        s[i] = 9
    while ind >0 and s[ind] < s[ind-1]:
        s[ind-1] = s[ind-1] -1
        s[ind] = 9
        ind -=1
    if s[0] == 0 and len(s) > 1: s= s[1:]
    return str(int("".join(map(str,s))))


t = int(input())
for i in range(1,t+1):
    s = map(int,list(input()))
    print("Case #%d: %s"%(i,solve(list(s))))
