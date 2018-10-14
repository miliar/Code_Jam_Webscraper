import sys

small = True
ipname, opname = sys.argv[1:3]

opf = open(opname, 'w')
ipf = open(ipname)


if small:
    maxval = 1001
else:
    maxval = 10**9

tidy = []
for x in range(1, maxval):
    xsplit = map(int, str(x))
    xsplit1 = [0] + xsplit
    xsplit1 = xsplit1[0:-1]
    cond = [False for a, b in zip(xsplit, xsplit1) if a<b]
    if len(cond):
        continue
    tidy.append(x)

T = int(ipf.readline())

digits = range(0, 10)
for t in range(1, T+1):
    Nstr = ipf.readline().strip()
    N = int(Nstr)
    ans = [ x for x in tidy if x<=N ][-1]
    opf.write('Case #%d: %d\n' % (t, ans))
opf.close()
