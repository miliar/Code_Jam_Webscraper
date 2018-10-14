
def test(matrix, n, m):
    """n = row, m = col
    [[1,2,3],]"""
    t_matrix = zip(*matrix)
    for i in range(0, n):
        for j in range(0, m):
            cur = matrix[i][j]
            max_row = max(matrix[i])
            max_col = max(t_matrix[j])
            if cur < max_row and cur < max_col:
                return 'NO'
    return 'YES'


def solve():
    fin = open("B-large.in", "r")
    fout = open("result.txt", "w")
    num_tests = int(fin.readline())
    for i in xrange(num_tests):
        line = fin.readline()  # bound
        table = []
        n, m = map(int, line.split())
        for _ in range(n):
            line = fin.readline()
            table.append([v for v in map(int, line.split())])

        check = test(table, n, m)
        fout.write("Case #%d: %s\n" % (i+1, check))
    fin.close()
    fout.close()


solve()
