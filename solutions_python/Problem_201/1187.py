infile = open("C-small-2-attempt1.in","r")
outfile = open("C-small2.txt","w")
def shalf(n):
    n -= 1
    if not n%2:
        return int(n/2)
    return int((n-1)/2)
def bhalf(n):
    n -= 1
    if not n%2:
        return int(n/2)
    return int((n+1)/2)
def enter(spaces):
    maxi = max(spaces.keys())
    spaces[maxi] -= 1
    if spaces[maxi] == 0:
        spaces.pop(maxi)
    smaller = shalf(maxi)
    bigger = bhalf(maxi)
    if smaller > 0:
        if not smaller in spaces.keys():
            spaces[smaller] = 0
        spaces[smaller] += 1
    if bigger > 0:
        if not bigger in spaces.keys():
            spaces[bigger] = 0
        spaces[bigger] += 1
        
def solve(n, k):
    spaces = {}
    spaces[n] = 1
    for i in range(k-1):
        enter(spaces)
    maxi = max(spaces.keys())
    return bhalf(maxi), shalf(maxi)

t = int(infile.readline())
for case in range(1, t+1):
    n, k = infile.readline().split()
    n = int(n)
    k = int(k)
    result = solve(n, k)
    maxi = result[0]
    mini = result[1]
    outfile.write("Case #{}: {} {}\n".format(case, maxi, mini))
infile.close()
outfile.close()
print("done")
        

