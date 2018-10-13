import sys

def get_rot(l):
    ret = [l]
    
    for i in range(0, len(l)-1):
        l2 = [x for x in ret[-1]]
        l2.append(l2.pop(0))
        ret.append(l2)
    return ret

def get_cyc(n):
    nlist = [digit for digit in str(n)]
    #print get_rot(nlist)
    ret = list(set([int("".join(num)) for num in get_rot(nlist) if num[0] != '0']))
    #print ret
    return ret


f = open('c.in', 'r')

times = int(f.readline())

for t in range(1,times+1):
    A, B = (int(num) for num in f.readline().split(' '))

    ans = 0
    for n in range(A, B+1):
        ans = ans + len(filter(lambda m: m > n and m <= B, get_cyc(n)))

    print 'Case #%d: %d' % (t, ans)
