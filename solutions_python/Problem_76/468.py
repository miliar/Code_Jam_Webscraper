# GCJ
# 2011
# Qualification Round
# Candy Splitting

# This is a Python script.
# It works with Python 2.6 on Windows XP.
# It reads from stdin and writes to stdout.

ntc = int(raw_input())

for tcn in range(1, ntc + 1):
    cc = int(raw_input())
    cvl = map(int, raw_input().split())
    xor = lambda x, y: x ^ y
    txo = reduce(xor, cvl)

    if txo:
        res = 'NO'
    else:
        res = sum(cvl) - min(cvl)

    print 'Case #{0}: {1}'.format(tcn, res)
