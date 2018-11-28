
def mkdir(path):
    cnt = 0
    dirs = path.split('/')[1:] # if path != '/' else ['']
    for i in xrange(len(dirs)):
        p = ''.join('/' + d for d in dirs[:i+1])
        if p not in FS:
            FS[p] = True
            cnt += 1

    return cnt

if __name__ == '__main__':
    for case in xrange(int(raw_input())):
        FS = {'/': True}
        N, M = [int(s) for s in raw_input().split()]
        for _ in xrange(N):
            path = raw_input()
            mkdir(path)

        res = 0
        for _ in xrange(M):
            path = raw_input()
            res += mkdir(path)

        print 'Case #%d: %d' % (case+1, res)
