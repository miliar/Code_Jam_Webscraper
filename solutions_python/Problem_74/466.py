# GCJ
# 2011
# Qualification Round
# Bot Trust

# This is a Python script.
# It works with Python 2.6 on Windows XP.
# It reads from stdin and writes to stdout.

ntc = int(raw_input())

for tcn in range(1, ntc + 1):
    tcd = raw_input().split()
    gt = 0
    rp = [1, 1]
    lmf = [0, 0]
    tdi = 1

    while tdi < len(tcd):
        cri = 0 if tcd[tdi] == 'B' else 1
        tdi += 1
        cbn = int(tcd[tdi])
        tdi += 1

        cmf = lmf[cri] + abs(cbn - rp[cri]) + 1
        gt = max(gt + 1, cmf)

        rp[cri] = cbn
        lmf[cri] = gt

    print 'Case #{0}: {1}'.format(tcn, gt);
