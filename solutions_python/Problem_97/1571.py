def recycle(a,b):
    c = str(a)
    return len(set([(a,c[x:]+c[:x]) for x in xrange(1, len(c)) if b > int(c[x:] + c[:x]) > a ]))
lines = open("C-small-attempt0.in").readlines()
out = open("out.txt","w")
y = 1
for line in lines[1:]:
    a, b = map(int, line.split())
    ans = sum([recycle(x,b+1) for x in xrange(a,b+1) if recycle(x,b+1) != []])
    write = "Case #%d: %d\n" % (y,ans)
    out.write(write)
    y += 1

out.close()
    
