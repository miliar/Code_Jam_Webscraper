
f = open('Asmall.in')
x=int(f.readline())

for times in range(1, x+1):
    set = f.readline()
    set.strip()
    #print set.split()
    #[n, m] = 
    num = set.split()
    n = int(num[0])
    m = int(num[1])
    
    path = {}   #name : [] all dirs

    for al in range(1, n+1):
        dir = f.readline()
        pt = dir.split('/')
        root = path
        for locs in pt:
            locs = locs.strip()
            if locs == '':
                continue
            if locs in root.keys():
                root = root[locs]
            else:
                root[locs] = {}
                root = root[locs]

    #root = path
    cnt = 0
    for nw in range(1, m+1):
        ndir = f.readline()
        pt = ndir.split('/')
        root = path
        for locs in pt:
            #locs.strip()
            if locs == '':
                continue
            #print locs
            locs = locs.strip()
            if locs in root.keys():
                root = root[locs]
            else:
                root[locs] = {}
                root = root[locs]
                cnt=cnt+1
    #print path, cnt
    print "Case #%d: %d"%(times,cnt)
                

