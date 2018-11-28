
def BotTrust():
    seq = raw_input().split()
    rseq = []
    bx, ox = 0, 0
    while len(seq) > 1:
        x = int(seq.pop())
        r = seq.pop()
        if r == "B":
            bx = x
        else:
            ox = x
        rseq.append( (r, bx, ox) )
    total = 0
    bx, ox = 1, 1
    for r, bx1, ox1 in reversed(rseq):
        if r == "B":
            dx = 1+abs(bx1-bx)
            bx = bx1
            ox = min(ox+dx, ox1) if ox1 > ox else max(ox-dx, ox1)
        else:
            dx = 1+abs(ox1-ox)
            ox = ox1
            bx = min(bx+dx, bx1) if bx1 > bx else max(bx-dx, bx1)
        total += dx
    print total

#---------------------------------------------------------------

T = int(raw_input())
for testcase in range(T):
    print "Case #%d:" % (testcase+1),
    BotTrust()
