from Queue import Queue

def print_cake(case_no, rows, cols, cake):
    q = Queue()
    for i in xrange(rows):
        for j in xrange(cols):
            if cake[i][j] != "?":
                q.put((i, j, cake[i][j]))
    
    moves=[(0,1),(0,-1)]
    while not q.empty():
        i, j, ch = q.get()
        for r, c in moves:
            if (0 <= i + r < rows) and (0<= j+c < cols) and cake[i+r][j+c] == "?":
                cake[i+r][j+c] = ch
                q.put((i+r, j+c, ch))

    q = Queue()
    for i in xrange(rows):
        for j in xrange(cols):
            if cake[i][j] != "?":
                q.put((i, j, cake[i][j]))
    moves=[(1,0),(-1,0)]
    while not q.empty():
        i, j, ch = q.get()
        for r, c in moves:
            if (0 <= i + r < rows) and (0<= j+c < cols) and cake[i+r][j+c] == "?":
                cake[i+r][j+c] = ch
                q.put((i+r, j+c, ch))

    print "Case #{0}:".format(case_no+1)
    for row in cake:
        print "".join(row)



if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(0, t):
        r, c = map(int, raw_input().split(" "))
        cake = []
        for j in xrange(r):
            cake.append(list(raw_input()))
        print_cake(i, r, c, cake)
