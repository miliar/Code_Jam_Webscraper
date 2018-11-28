T = int(raw_input())

for t in range(T):
    N,M = map(int, raw_input().split(' '))

    dir_exist = set()
    dir_create = set()

    for n in range(N):
        dirs = raw_input().split('/')
        for i in range(1,1+len(dirs)):
            dir_exist.add('/'.join(dirs[:i]))
    for m in range(M):
        dirs = raw_input().split('/')
        for i in range(2, 1+len(dirs)):
            dir = '/'.join(dirs[:i])
            if dir not in dir_exist:
                dir_create.add(dir)

    print "Case #%d: %d" % (t+1, len(dir_create))
