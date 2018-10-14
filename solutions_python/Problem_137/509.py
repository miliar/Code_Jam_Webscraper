
def range_check(x, y):
    return x >= 0 and x < r and y >= 0 and y < c

def print_solution(not_tried, tried):
    matrix = [['*' for x in range(c)] for x in range(r)]

    for i in tried:
        matrix[i[0]][i[1]] = '.'
    for i in not_tried:
        matrix[i[0]][i[1]] = '.'
    first = tried[0]
    matrix[first[0]][first[1]] = 'c'

    for i in range(r):
        s = ''
        for j in range(c):
            s += matrix[i][j]
        s += '\n'
        out.write(s)


def recursion(not_tried, tried):
    #print("not tried: %s\ntried:%s" % (not_tried, tried))
    for k in not_tried:
        nnt, nt = stamp(k[0], k[1], not_tried[:], tried[:])
        sum_len = len(nnt) + len(nt)
        if sum_len == empty:
            print_solution(nnt, nt)
            return True
        elif sum_len > empty:
            return False
        else:
            if recursion(nnt, nt):
                return True


def stamp(x, y, not_tried, tried):
    not_tried.remove((x,y))
    tried.append((x,y))
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if range_check(i,j):
                if not ((i,j) in tried or (i,j) in not_tried):
                    not_tried.append((i,j))
    return not_tried, tried

fin = open('a.in', 'r')
out = open('a.out','w')
n = int(fin.readline())
print(n)

for i_case in range(n):
    print('Case #%d:' % (i_case+1))
    out.write('Case #%d:\n' % (i_case+1))
    r, c, m = map(int, fin.readline().split())
    print("%d %d %d" % (r, c, m))
    #out.write("%d %d %d\n" % (r, c, m))

    empty = r * c - m
    #print ("%d" % empty)
    #print(matrix)
    if empty == 1:
        print_solution([],[(0,0)])
        continue

    not_tried = [(0,0)]
    tried = []
    b = recursion(not_tried, tried)
    if not b:
        #for i in range(r):
        #    for j in range(c):
        #        not_tried = [(i,j)]
        #        tried = []
        #        b = recursion(not_tried, tried)
        #        if b:
        #            break
        #    if b:
        #        break
        if not b:
            print('Impossible')
            out.write('Impossible\n')

    #print("len %d" % len(sum))


