import sys
import pprint

def main():
    t = int(sys.stdin.readline())
    for k in range(t):
        fail = False
        line = sys.stdin.readline().split()
        n = int(line[0])
        m = int(line[1])
        g = []
        for i in range(n):
            line = sys.stdin.readline().split()
            g.append([])
            for j in range(m):
                g[i].append(int(line[j]))
                if int(line[j]) > 100:
                    fail = True
        max_row = []
        for i in range(n):
            max_row.append(0)
            for j in range(m):
                max_row[i] = max(max_row[i], g[i][j])
        max_col = []
        for j in range(m):
            max_col.append(0)
            for i in range(n):
                max_col[j] = max(max_col[j], g[i][j])
        for i in range(n):
            for j in range(m):
                if g[i][j] < max_col[j] and g[i][j] < max_row[i]:
                    fail = True
                    break
            if fail:
                break
        if fail:
            print 'Case #{}: NO'.format(k + 1)
        else:
            print 'Case #{}: YES'.format(k + 1)

main()