depth = 0
width = 0

def solve(graph):
    # print depth, width
    done = [[False for b in range(width)] for a in range(depth)]
    for i in range(depth):
        m = max(graph[i])
        # print m
        for j in range(width):
            if graph[i][j] == m:
                done[i][j] = True
    for i in range(width):
        m = max([graph[x][i] for x in range(depth)])
        # print m
        for j in range(depth):
            if graph[j][i] == m:
                done[j][i] = True
    for i in range(depth):
        for j in range(width):
            if (not done[i][j]):
                return "NO"
    return "YES"








f = open('inin.in', 'r')
out = open('Aoutput', 'w')
l = f.readline()
num = int(l)
for i in range(num):
    l = f.readline()
    sp = l.split()
    depth = int(sp[0])
    width = int(sp[1])
    graph = [[0 for b in range(width)] for a in range(depth)]
    for j in range(depth):
        l = f.readline()
        sp = l.split()
        for k in range(width):
            graph[j][k] = int(sp[k])
    # f.readline()
    # import pdb; pdb.set_trace()
    print "Case #{0}: {1}".format(i+1, solve(graph))