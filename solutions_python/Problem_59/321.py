f = open("A-large.in")
T = int(f.readline())
out = open("A-large.out", "w")

for i in range(T):
    N, M = [int(x) for x in f.readline().split()]
    dirs = []
    for j in range(N):
        dirs.append(f.readline()[1:].strip())

    ndirs = []
    for j in range(M):
        ndirs.append(f.readline()[1:].strip())

    tree = {}
    for d in dirs:
        cur = tree
        for fold in d.split("/"):
            if not fold in cur:
                cur[fold] = {}
            
            cur = cur[fold]

    count = 0
    for d in ndirs:
        cur = tree
        for fold in d.split("/"):
            if not fold in cur:
                count += 1
                cur[fold] = {}

            cur = cur[fold]

    out.write("Case #%d: %d\n" % (i+1, count))

out.close()
f.close()