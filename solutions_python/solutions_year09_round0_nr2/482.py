import sys

(T) = int(sys.stdin.readline())

for t in range(T):
    (Y, X) = sys.stdin.readline().split()
    X = int(X)
    Y = int(Y)

    alt = {}
    col = {}

    adj = {}

    def get_dir(x, y):
        min_h = alt[(x,y)]
        next_x = x
        next_y = y

        dx = [0, -1, 1, 0]
        dy = [-1, 0, 0, 1]

        for d in range(4):
            if ((x+dx[d],y+dy[d]) in alt) and alt[(x+dx[d],y+dy[d])] < min_h:
                min_h = alt[(x+dx[d],y+dy[d])]
                next_x = x+dx[d]
                next_y = y+dy[d]

        return (next_x, next_y)

    def add_adj(x1,y1,x2,y2):
        if (x1,y1) not in adj:
            adj[(x1,y1)] = []
        adj[(x1,y1)].append((x2,y2))
        if (x2,y2) not in adj:
            adj[(x2,y2)] = []
        adj[(x2,y2)].append((x1,y1))

    for i in range(Y):
        line = sys.stdin.readline().strip().split()
        for j in range(X):
            alt[(j,i)] = line[j]

    for i in range(Y):
        for j in range(X):
            next_x, next_y = get_dir(j,i)
            if next_x != j or next_y != i:
                add_adj(j,i,next_x,next_y)

    def color(x, y, letter):
        queue = [(x,y)]
        while queue:
            cur = queue.pop()
            col[cur] = letter
            if cur in adj:
                for adja in adj[cur]:
                    if adja not in col:
                        queue.append(adja)

    curl = 'a'
    for i in range(Y):
        for j in range(X):
            if (j,i) not in col:
                color(j,i, curl)
                curl = chr(ord(curl) + 1)

    print 'Case #%d:' % (t+1)
    for i in range(Y):
        for j in range(X):
            print col[(j,i)],
        print
