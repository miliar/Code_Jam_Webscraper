

def toTidy(n):
    for j in range(len(n)-1):
        d = n[j+1]-n[j]
        if d>0:
            nn = list(n[j+1:])
            nn[0]=nn[0]-1
            nn[0]=nn[0] if nn[0]>=0 else 9
            nextn = toTidy(nn)
            return [9]*(j+1)+nextn
    return n

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    N = [int(x) for x in list(input())][::-1]
    res = int("".join([str(x) for x in toTidy(N)[::-1]]))
    print("Case #{}: {}".format(i, res))
    # check out .format's specification for more formatting options
