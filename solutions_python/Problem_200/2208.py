def int2list(i):
    l = []
    for d in str(i):
        l.append(int(d))
    return l

def list2int(l):
    num = 0
    ex = 0
    for j in range(len(l)-1, -1, -1):
        num += l[j]*10**ex
        ex += 1
    return num


def getmaxtidy(n):
    ln = int2list(n)
    start9 = -1
    for i in range(0, len(ln)-1):
        if ln[i] > ln[i+1]:
            ln[i] -= 1
            i-=1
            while i >= 0 and ln[i] > ln[i+1]:
                ln[i] -= 1
                i -= 1
            start9 = i+2
            break
    if start9 >= 0:
        for i in range(start9, len(ln)):
            ln[i] = 9
        return list2int(ln)
    else:
        return n



t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    print("Case #{}: {} ".format(i, getmaxtidy(n)))


