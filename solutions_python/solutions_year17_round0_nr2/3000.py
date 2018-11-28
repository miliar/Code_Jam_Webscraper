def solve():
    s = list(input())
    for i in range(len(s)):
        if i < len(s) - 1 and int(s[i]) > int(s[i+1]):
            k = s[i]
            f = True
            for j in range(len(s)):
                if s[j] == k and f:
                    f = False;
                    s[j] = str(int(s[j]) - 1);
                elif not f:
                    s[j] = '9'
            break
    i = 0
    while i < len(s) and s[i] == '0':
        s[i] = ''
        i += 1
    return "".join(s)


T = int(input())

for t in range(T):
    print("Case #"+str(t+1) +": " + str(solve())) 
