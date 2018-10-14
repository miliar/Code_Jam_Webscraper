import fileinput

def checkMax(m):
    r = []
    ang = 0
    for a in m:
        if ang < a:
            ang = a
    for i in range(len(m)):
        if m[i] < ang:
            r.append(i)
    return r

def toInts(m):
    r = []
    ang = m.split(' ')
    for a in ang:
        r.append(int(a))
    return r

def solve():
    inf = open('fuck')
    content = inf.readlines()
    inf.close()

    outf = open('out', 'w')

    T = int(content[0])
    cnt = 1
    flag = False
    for n in range(T):
        flag = False
        print cnt
        N = int(content[cnt].split(' ')[0])
        M = int(content[cnt].split(' ')[1])
        print '- ' + str(N) + ' ' + str(M)
        cnt = cnt + 1
        for a in range(N):
            print content[cnt + a]
            smaller = checkMax(toInts(content[cnt + a]))
            print smaller
            # for columns smaller than max
            for i in smaller:
                for j in range(N):
                    print str(cnt + a) + ' ' + str(cnt + j)
                    if int((content[cnt + a].split(' '))[i]) < int((content[cnt + j]).split(' ')[i]):
                        outf.write('Case #%d: NO\n'%(n+1))
                        cnt = cnt + N

                        flag = True
                        break
                if flag:
                    break
            if flag:
                break
        if flag:
            continue
        outf.write('Case #%d: YES\n'%(n+1))
        cnt = cnt + N
    outf.close()
