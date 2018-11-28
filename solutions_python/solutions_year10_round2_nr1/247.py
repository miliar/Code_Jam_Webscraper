import sys

def process_input(openfile):
    #openfile = open(filename, 'r')
    T = int(openfile.readline()[:-1])
    tests = []
    for j in range(T):
        NK = openfile.readline()
        N, K = [int(s) for s in NK.split(' ')]
        board = []
        for i in range(N):
            row_st = openfile.readline()[:-1]
            row = list(row_st)
            board.append(row)
        tests.append([N, K, board])
    return tests



if __name__ == '__main__':
    ### PROGRAM AAAAAAAAAAA
    #openfile = open('A.in', 'r')
    openfile = sys.stdin
    ET = int(openfile.readline()[:-1])
    for T in range(1, ET+1):
        # read test data
        NM = openfile.readline()
        N, M = [int(s) for s in NM.split(' ')]
        dirs_have = ['/']
        for j in range(N):
            sdir = openfile.readline()[:-1]
            dirs_have.append(sdir)
        dirs_want = ['/']
        for j in range(M):
            sdir = openfile.readline()[:-1]
            dirs_want.append(sdir)
        # compute
        mkdirs = 0
        for sdir in dirs_want:
            dir_parts = sdir.split('/')[1:]
            pdir = ''
            for j in dir_parts:
                pdir = pdir + '/' + j
                if not pdir in dirs_have:
                    dirs_have.append(pdir)
                    mkdirs += 1
        print 'Case #%s: %s' %(T, mkdirs)
    openfile.close()
