def build_tree(paths):
    root = {}
    for path in paths:
        nodes = [i.strip() for i in path.split("/") if i]
        cur = root
        for node in nodes:
            cur[node] = cur.get(node, {})
            cur = cur[node]
    return root

def add_paths_to_tree(root, paths):
    cnt = 0
    for path in paths:
        nodes = [i.strip() for i in path.split("/") if i]
        cur = root
        for node in nodes:
            if node not in cur:
##                print "adding ", node
                cnt += 1
                cur[node] = {}
            cur = cur[node]
##        print ""
    return cnt

def parse_input_and_output(infile, outfile):
    lines = open(infile).readlines()
    T = int(lines[0])
    cnt = 1
    R = []
    for i in range(T):
        try:
            t = lines[cnt].split()
            N = int(t[0])
            M = int(t[1])
            tree = build_tree(lines[cnt+1:cnt+1+N])
##            print tree
            res = add_paths_to_tree(tree, lines[cnt + 1 + N:cnt + 1 + N + M])
            R.append("Case #%d: %s" % (i + 1, res))
            cnt += 1 + N + M
        except (IndexError, ValueError):
            pass
    open(outfile, "w").write("\n".join(R))

