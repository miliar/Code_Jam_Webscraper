f = [l[:-1] for l in file("in")]
cases = int(f[0])

f=f[1:]

def dirSplit(str):
    res = set()

    if str[-1] != "/": str+= "/"
    str = str.split("/")


    for x in range(1, len(str)):
        new = "/".join(str[0:x])
        res.add(new)
    res.remove('')
    return res


case=0
for x in range(cases):
    case +=1
    exists, create = [int(x) for x in f[0].split(" ")]
    f=f[1:]
    all_dirs = set()
    for x in range(exists):
        new_dirs = dirSplit(f[0])
        all_dirs = all_dirs.union(new_dirs)
        f=f[1:]

    res=0
    for x in range(create):
        new_dirs = dirSplit(f[0])
        for dir in new_dirs:
            if dir not in all_dirs:
                res+=1
            all_dirs.add(dir)
        f=f[1:]

    print "Case #%d: %d" % (case, res)
