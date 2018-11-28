def bottrust(N, path):
    posO, posB = [], []
    for robot,x in path:
        if robot=='O': posO.append(x)
        else: posB.append(x)
    xO, xB=1,1
    itO, itB=iter(posO), iter(posB)
    try: next_xO=itO.next()
    except StopIteration: next_xO=101
    try: next_xB=itB.next()
    except StopIteration: next_xB=101
    ans=0
    for robot, next_x in path:
        if robot=='O': #next_x == next_xO:
            try: next_xO=itO.next()
            except StopIteration: next_xO=101
            dx = abs(next_x-xO)+1
            ans += dx
            xO = next_x
            if next_xB<xB: xB=max(next_xB,xB-dx)
            else: xB=min(xB+dx, next_xB)
            #print 'O', xO, '- B', xB, ans
        else:
            try: next_xB=itB.next()
            except StopIteration: next_xB=101
            dx = abs(next_x-xB)+1
            ans += dx
            xB = next_x
            if next_xO<xO: xO=max(next_xO,xO-dx)
            else: xO=min(xO+dx, next_xO)
            #print 'B', xB, '- O', xO, ans
    return ans

if __name__ == '__main__':
    fi = open('inputA.txt', 'r')
    fo = open('outputA.txt', 'w')
    T = int(fi.readline().strip('\n\r '))
    for ix,l in enumerate(fi, start=1):
        ls = l.strip('\n\r ').split(' ')
        res = bottrust(int(ls[0]), zip(ls[1::2], map(int, ls[2::2])))
        #print res
        fo.write('Case #%d: %d\n' % (ix, res))
