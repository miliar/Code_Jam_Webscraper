import os.path

already_created = {}
need_create = []

def create(p):
    if p in already_created:
        return 0
    if p == '/':
        return 0
    dirname = os.path.dirname(p)
    ret = create(dirname) + 1
    already_created[p] = ''
    return ret

fin = open("A-large.in", "r")
fout = open("A.out", "w")



T = int( fin.readline() )

for case in xrange(1, T+1):
    line = fin.readline()
    s_line = line.strip('\n').split(' ')
    N = int(s_line[0])
    M = int(s_line[1])
    already_created = {}
    need_create = []
    
    for al in xrange(N):
        line = fin.readline().strip('\n')
        already_created[line] = ''

    for ne in xrange(M):
        line = fin.readline().strip('\n')
        need_create += [line, ]

    need_create.sort()

    ans = 0
    
    for p in need_create:
        ans += create(p)

    fout.write("Case #%d: %d\n" % (case, ans) )

fin.close()
fout.close()

