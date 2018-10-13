import sys

xAND = 1
xOR = 0
MAX=1000000

def change(v, node):
    if(node[0] == v):
        return 0
    if(node[1] == 1):
        return 1
    return MAX

def solve(nodes, k, v):
    node = nodes[k]
    if(node[2] >= 0):
        if(node[0] == v):
            return 0
        else:
            return MAX
    left = k*2 + 1
    right = k*2 + 2
    if(v == 0):
        costl = solve(nodes, left, 0)
        costr = solve(nodes, right, 0)
        costand = min(costl, costr) + change(xAND, node)
        costor = costl + costr + change(xOR, node)
    else:
        costl = solve(nodes, left, 1)
        costr = solve(nodes, right, 1)
        costand = costl + costr + change(xAND, node)
        costor = min(costl,costr) + change(xOR, node)
    return min(costor, costand)

for case in range(1, int(sys.stdin.readline())+1):
    (M, V) = map(int, sys.stdin.readline().split(' '))
    nodes = []
    for i in range((M-1)/2):
        node = map(int, sys.stdin.readline().split(' '))
        node.append(-1)
        nodes.append(node)
    for i in range((M+1)/2):
        node = [int(sys.stdin.readline()), 0, 1]
        nodes.append(node)
        
    xmin = solve(nodes, 0, V)
    if(xmin >= MAX):
        print "Case #%d: IMPOSSIBLE" % case
    else:
        print "Case #%d: %d" % (case, xmin)
        
