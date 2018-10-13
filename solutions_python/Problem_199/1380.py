from Queue import Queue


def con(S, K):
    ret = []
    for pos in range(len(S)-K+1):
        tmp = list(S)
        for i in range(pos, pos + K):
            if tmp[i] == '+':
                tmp[i] = '-'
            else:
                tmp[i] = '+'
        ret.append(''.join(tmp))
    return ret

fin = open("A-small-attempt0.in")
T = int(fin.readline())
fout = open('A_output.txt', 'w')
for t in range(1, T + 1):
    S, K = fin.readline().strip().split(' ')
    K = int(K)
    target = '+' * len(S)
    open = set()
    open.add(S)
    Q = Queue()
    Q.put((S, 0))
    res = "Case #%s: %s\n" % (t, "IMPOSSIBLE")
    flag = False
    while Q.qsize() > 0:
        now, deep = Q.get()
        if now == target:
            res = "Case #%s: %s\n" % (t, deep)
            flag = True
            break
        for nc in con(now, K):
            if nc in open:
                continue
            open.add(nc)
            Q.put((nc, deep + 1))
    fout.write(res)
fin.close()
fout.close()