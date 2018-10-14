flips = 'ay bh ce ds eo fc gv hx id ju ki lg ml nb ok pr qz rt sn tw uj vp wf xm ya zq'.split()
flips.append("  ")
flips = dict(flips)
N = int(raw_input())
for i in range(1, N+1):
    s = raw_input()
    n = ''
    for c in s:
        n = n+flips[c]
    print "Case #"+str(i)+": " + n
