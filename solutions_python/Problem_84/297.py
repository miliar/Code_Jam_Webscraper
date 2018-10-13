from sys import argv


def open_file(filename):
    fin = open(filename)
    num_of_tests = int(fin.readline())
    for i in xrange(num_of_tests):
        rowcols = fin.readline().split()
        rows = int(rowcols[0])
        cols = int(rowcols[1])
        mat = []
        for j in xrange(rows):
            mat.append(list(fin.readline().strip()))
        solve(i+1, rows, cols, mat)
    fin.close()

def solve(num, rows, cols, mat):
    print "Case #%s:" %(num)
    for i in xrange(len(mat)-1):
        row = mat[i]
        for c in xrange(len(row)-1):
            if row[c] == '#':
                imt_row = mat[i+1]
                if row[c+1] == '#' and imt_row[c] == '#' and imt_row [c+1] == '#':
                    row[c], row[c+1], imt_row[c], imt_row[c+1] = '/', '\\', '\\', '/'
                else:
                    print "Impossible"
                    return
    for c in mat:
        for k in c:
            if k == '#':
                print "Impossible"
                return
    for c in mat:
        print ''.join(c)

open_file(argv[1])
