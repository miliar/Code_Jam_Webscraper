def gen(s,i):
    sp = [{'1'},{'0','1'}]
    if set(s[:i]) in sp:
        return '9'*(len(s[:i])-1)+'9'*(len(s)-len(s[:i]))
    if len(set(s[:i])) == 1:
        return str(int(s[0])-1)+'9'*(len(s)-1)
    return str(int(s[:i])-1)+'9'*(len(s)-len(s[:i]))

t = int(input())
for i in range(1,t+1):
    n = str(int(input()))
    p = True
    for j in range(1,len(n)):
        if n[j] < n[j-1]:
            n = gen(n,j)
            p = False
            break
    print("Case #{}: {}".format(i,n))
            
