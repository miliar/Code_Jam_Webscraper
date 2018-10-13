a = []

def isok(n):
    n = list(str(n))
    if n == sorted(n):
        return True
    return False

for i in range(1,1001):
    if isok(i):
        a.append(i)

for i in range(1,input()+1):
    z = input()
    if z >= 999:
        print "Case #{}: {}".format(i,a[-1])
        continue
    m = 0
    for j in range(len(a)):
        if a[j] > z:
            m = j
            break
    print "Case #{}: {}".format(i, a[m-1])
