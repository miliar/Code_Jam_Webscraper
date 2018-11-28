def solve(s):
    s = list(s)
    for i in range(len(s)-1):
        if int(s[i])>int(s[i+1]):
            return solve(list(str(int(''.join(s[:i+1]))-1)))+['9']*(len(s)-i-1)
    return s

filename = "B-large.in"
f = open(filename,"r")
fout = open(filename.replace(".in", ".out"), "w")
N = int(f.readline())
for i in range(N):
    res = int(''.join(solve(f.readline().strip())))
    print("Case #{}:".format(i+1), res)
    print("Case #{}:".format(i+1), res, file=fout)
f.close()
fout.close()
