

#grid = [[-1,0,-1],[0,-1,25],[-1,25,-1]]
#grid = [[0,3],[2,-1]]


def add_dir(cur, dir):
    c=0
    #print cur, "+=", dir
    for i in range(1,len(dir)):
        if dir[i]=="/":
            if dir[:i] not in cur:
                cur.add(dir[:i])
                c+=1
    if dir not in cur:
        cur.add(dir)
        c+=1
    #print c
    return c


input = open("e:/A-large.in", "r")
for testcase in range(1, int(input.readline())+1):
    n, m = map(int, input.readline().split(' '))
    #print R,C
    c=0
    root = set()
    root.add("/")
    for _ in range(n):
        add_dir(root, input.readline().strip())
    for _ in range(m):
        c+=add_dir(root, input.readline().strip())
    #print 'grid:', grid
    print "Case #%d:"%testcase, c


