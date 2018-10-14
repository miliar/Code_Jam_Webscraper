from lxml import etree


TEMPLATE = "Case #%d: %d"

def mkdir(tree, path):
    path_splitted = path.split("/")
    num = 0

    cur = tree
    for dir in path_splitted[1:]:
        child = cur.find("s" + dir)
        if child is None:
            cur.append(etree.Element("s" + dir))
            cur = cur.find("s" + dir)
            num = num + 1
        else:
            cur = child

    return num


f = file('A-large.in')
T = int(f.readline())

for i in range(T):
    tree = etree.Element("root")
    (N, M) = map(int, f.readline().split())

    dirs = []
    cur = dirs
    for j in range(N):
        path = f.readline()
        mkdir(tree, path[:len(path)-1])

    nums = 0
    for j in range(M):
        path = f.readline()
        num = mkdir(tree, path[:len(path)-1])
        nums = nums + num

    print TEMPLATE % (i + 1, nums)
