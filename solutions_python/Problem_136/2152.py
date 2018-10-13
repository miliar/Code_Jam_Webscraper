def solve(l):
    c,f,x = float(l[0]),float(l[1]),float(l[2])
    t = 0
    r = 2
    mc = x/r
    mb = c/r + c/f
    while mc>mb:
        t+=c/r
        r+=f
        mc = x/r
        mb = c/r + c/f
    t+=mc
    return '{:.7f}'.format(t)

output = []
with open('B-large.in','r') as infile:
    n = int(infile.readline().rstrip())
    for i in range(n):
        output.append('Case #' + str(i+1) + ': ' + solve(infile.readline().rstrip().split()))

with open('B-large.out','w') as outfile:
    outfile.write('\n'.join(output))
