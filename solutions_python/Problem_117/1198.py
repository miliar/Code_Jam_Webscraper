fin = open('b.in', 'r')
fout = open('b.out', 'w')

def check(lawn, n, m):
    for h in range(100):
        for x in range(n):
            for y in range(m):
                if lawn[x][y] == h:
                    col = True
                    for i in range(n):
                        if lawn[i][y] != h:
                            col = False
                            break
                    if (not col) and lawn[x].count(h) < m:
                        return 'NO'

        for x in range(n):
            for y in range(m):
                if lawn[x][y] == h:
                    lawn[x][y] += 1
    return 'YES'

total_test_cases = int(fin.readline())
for test_case_num in range(total_test_cases):
    (n, m) = map(int, fin.readline().split())
    lawn = []
    for i in range(n):
        lawn.append(map(int, fin.readline().split()))
    print >> fout, 'Case #' + str(test_case_num + 1) + ':',\
            check(lawn, n, m)
