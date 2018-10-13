def flip(s):
    if s == '+':
        return '-'
    else:
         return '+'

def flipString(s):
    res = ""
    for i in range(0, len(s)):
        res = res + flip(s[i])
    return res

T = int(input())
for t in range(T):
    i = input().split()
    s = i[0]
    k = int(i[1])
    cont = 0
    for i in range(0, len(s)-k+1):
        if s[i] == '-':
            s = s[:i]+flipString(s[i:i+k])+s[i+k:]
            cont += 1
        #print(s)
    res = cont
    if s.count('-') != 0:
        res = "IMPOSSIBLE"
    print("Case #{}: {}".format(t+1, res))
