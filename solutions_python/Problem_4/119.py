def product(v1,v2):
    p = 0
    for i in range(len(v1)):
        p += v1[i]*v2[i]
    return p

def perm2(v1,v2):
    v1.sort()
    v2.sort()
    v2.reverse()
    return product(v1,v2)
    
T = int(raw_input())
for i in range(T):
    raw_input()
    v1 = raw_input()
    v2 = raw_input()
    v1 = v1.split(' ')
    v2 = v2.split(' ')
    v1 = [int(ii) for ii in v1]
    v2 = [int(ii) for ii in v2]
    print "Case #" + str(i+1) + ": " + str(perm2(v1,v2))

