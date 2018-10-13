


def build_existing_tree(f,n):
    tree = {}
    for i in range(n):
        curr_tree = tree
        for d in f.readline().strip().split("/")[1:]:
            curr_tree = curr_tree.setdefault(d,{})
    return tree


def count_mkdirs(f,n,m):
    tree = build_existing_tree(f,n)
    count = 0
    for i in range(m):
        curr_tree = tree
        for d in f.readline().strip().split("/")[1:]:
            if not curr_tree.has_key(d):
                count += 1
                curr_tree[d] = {}
            curr_tree = curr_tree[d]
    return count

f = open("A-large.in")

k = int(f.readline().strip())

with open("output1.txt", "w") as outf:
    for i in range(k):
        ts = f.readline().strip().split()
        n = int(ts[0])
        m = int(ts[1])
        r = count_mkdirs(f, n, m)
        outf.write("Case #%d: %d\n" % ((i+1), r))
        