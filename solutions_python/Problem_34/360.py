import re, itertools
r = re.compile("(\(\w+\)|\w)")
s = open('c:\\A-small-attempt0.in','r').readlines()
L,D,N = map(lambda x: int(x), s[0].split())
words = map(lambda x: x.strip(), s[1:D+1])
patterns = map(lambda x: x.strip(), s[D+1:D+N+1])
for x,pattern in enumerate(patterns):
    i = 0
    fl = False
    allowed_lists = map(lambda x: x[1:-1] if x[0]=='(' else x,
                        r.findall(pattern))
    if len(allowed_lists) != L:
        continue
    for word in words:
        fl = True
        for liter, allowed_list in itertools.izip(word, allowed_lists):
            if liter not in allowed_list:
                fl=False
                break
        if fl:
            i+=1

    print "Case #%s: %s" %(x+1,i)

