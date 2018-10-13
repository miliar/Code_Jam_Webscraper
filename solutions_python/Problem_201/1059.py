def ceil(n):
    if n>int(n):
        return int(n)+1
    return int(n)
def solve(n, k):
    r,l = ceil((n-1)/2), int((n-1)/2)
    if k==1:
        return r,l
    if k%2:
        return solve(l ,int((k-1)/2))
    return solve(r, ceil((k-1)/2))
    
    

filename = "C-small-2-attempt0.in"
f = open(filename,"r")
fout = open(filename.replace(".in", ".out"), "w")
N = int(f.readline())
for i in range(N):
    a,b = f.readline().split(' ')
    res = '{} {}'.format(*solve(int(a.strip()), int(b.strip())))
    print("Case #{}:".format(i+1), res)
    print("Case #{}:".format(i+1), res, file=fout)
f.close()
fout.close()
