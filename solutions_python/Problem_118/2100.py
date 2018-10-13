def isFair(nbre):
    from copy import deepcopy
    nbre = list(str(nbre))
    nbre_ = deepcopy(nbre)
    nbre.reverse()
    return nbre_ == nbre

def main(lst):
    nbre = 0
    i = lst[0]
    while i <= lst[1]:
            if isFair(i):
                x = int(i**0.5)
                if x**2 == i and isFair(x):
                        nbre += 1
            i += 1
    return nbre

if __name__ == '__main__':
    f = open('in','r')
    g = open('out','w')

    t = int(f.readline()) + 1
    for i in xrange(1,t):
        lst = map(int, f.readline().split())
        res = 'Case #%d: %d\n' % (i,main(lst))
        g.write(res)
    f.close()
    g.close()

