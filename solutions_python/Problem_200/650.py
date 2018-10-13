def isTidy(n):
    l = []
    while n > 0:
        l.append(n % 10)
        n /= 10
    l.reverse()
    for i in range(len(l)-1):
        if l[i+1] < l[i]:
            return False
    return True

def alg(n):
    l = []
    while n > 0:
        l.append(n % 10)
        n /= 10
    for i in range(len(l) - 1):
        if l[i] < l[i+1]:
            l[i+1] -= 1
            for j in range(i+1):
                l[j] = 9
    l.reverse()
    ans = 0
    for i in l:
        ans = ans * 10 + i
    return ans


#for i in range(1,10000):
#    print i,
    #for j in range(i, 0, -1):
    #    if isTidy(j):
    #        print j
    #        break
#    print alg(i)
t = input()
for poo in range(t):
    n = input()
    print "Case #" + str(poo + 1) + ":",
    print alg(n)
