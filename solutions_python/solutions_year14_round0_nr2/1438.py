filename = 'a.in'
out = open('a.out', 'w+')
s = open(filename)
t = int(s.readline())
for tc in range(t):
    c, f, x = (float(p) for p in s.readline().split())
    y = int(float(x*f - 2*c)/float(c*f))
    if y < 0:
        y = 0
    total = 0
    for k in range(y):
        total += float(c)/float(2+k*f)
    total += float(x)/float(2+y*f)
    out.write('Case #{0}: {1}\n'.format(tc+1, total))
    

