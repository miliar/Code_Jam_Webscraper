def rev(z):
    s = str(z)
    if s[-1] == '0':
        return None
    else:
        return int(s[::-1])

results = {1 : 1}
c = 1
M = 1000000
for x in range(2, M+1):
    y = rev(x)
    if y is None:
        results[x] = results[x-1] + 1
    elif y < x:
        results[x] = min(results[y]+1, results[x-1] + 1)
    else:
        results[x] = results[x-1] + 1

# for x in sorted(results.keys()):
#     print x, results[x]

inputfile = 'A-small-attempt4.in'
g = open(inputfile, 'r+b')
T = int(g.readline().strip())

for i in range(1, T+1):
    N = int(g.readline().strip())
    print "Case #%d: %d" % (i, results[N])
