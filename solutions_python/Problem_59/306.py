#f = open("/home/roy/sample-in.txt")
f = open("/home/roy/Downloads/A-large.in")

lines = f.readlines()
count = int(lines[0])

#print "There are %s cases" % count

idx = 1
for i in range(0, count):
    line1 = lines[idx]
    idx = idx + 1

    [N, M] = [int(a) for a in line1.rstrip().split(" ")]
    root = {}
    for n in range(0, N):
        exist1 = lines[idx].rstrip()
        curr = root
        for node in exist1[1:].split("/"):
            if curr.has_key(node):
                curr = curr[node]
            else:
                curr[node] = {}
                curr = curr[node]
        idx = idx + 1
    create = 0
    for m in range(0, M):
        create1 = lines[idx].rstrip()
        curr = root
        for node in create1[1:].split("/"):
            if curr.has_key(node):
                curr = curr[node]
            else:
                curr[node] = {}
                curr = curr[node]
                create = create + 1
        idx = idx + 1
    
    #print str(root)
    print "Case #%d: %s" % (i+1, create)
