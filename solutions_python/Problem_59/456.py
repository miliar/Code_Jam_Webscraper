def fixit(dirs, dir):
    l = dir.split("/")
    cnt = 0
    add = []
    d = dir
    add.append(d)
    while len(l) > 1 and d not in dirs:
        #print "d not in dirs:", d, dirs, l
        l.pop()
        cnt += 1
        d = "/".join(l)
        add.append(d)
    map(lambda dir : dirs.add(dir), add)
    #print "fixit return:", dirs, cnt, l, add, d
    return cnt


import sys
f = open(sys.argv[1], 'r')
t = int(f.readline())
case = 0
while t>0:
    count = 0
    dirs = set()
    nums = map(int,f.readline().split())
    while nums[0]>0:
        dirs.add(f.readline().strip()) 
        nums[0] -= 1
    #print "existing:...", dirs
    while nums[1]>0:
        count += fixit(dirs, f.readline().strip())
        #print "zzz...", count
        nums[1] -= 1
    t -= 1
    case += 1
    print "Case #%d: %s" % ( case, count )
    #print "done with dirs:", dirs

