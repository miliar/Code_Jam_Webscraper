def solve(s, K):
    n = 0
    s = list(s.strip())
    K = int(K.strip())
    for i in range(len(s)-K+1):
        if s[i]=='-':
            n += 1
            for j in range(K):
                s[i+j] = '-' if s[i+j]=='+' else '+'
    if len(set(s))>1:
        return 'IMPOSSIBLE'
    return str(n)

filename = "A-large.in"
f = open(filename,"r")
fout = open(filename.replace(".in", ".out"), "w")
N = int(f.readline())
for i in range(N):
    res = solve(*f.readline().split(' '))
    print("Case #{}:".format(i+1), res)
    print("Case #{}:".format(i+1), res, file=fout)
f.close()
fout.close()
