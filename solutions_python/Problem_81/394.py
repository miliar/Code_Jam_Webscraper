# GCJ
# 2011
# Round 1B
# RPI

# This is a Python script.
# It works with Python 2.6 on Windows XP.
# It reads from stdin and writes to stdout.

ntc = int(raw_input())

for tcn in range(1, ntc + 1):
    tmn = int(raw_input())
    tpl = [raw_input() for ti in range(tmn)]
    tgl = map(lambda x: sum(map(lambda y: 0 if y == '.' else 1, x)), tpl)
    twl = map(lambda x: sum(map(lambda y: 1 if y == '1' else 0, x)), tpl)
    twp = [float(twl[ti]) / tgl[ti] for ti in range(tmn)]
    owa = [0.] * tmn

    for ti in range(tmn):
        tip, tiw = tpl[ti], twl[ti]
        tigm1, tiwm1 = float(tgl[ti] - 1), tiw - 1

        for tj in range(tmn):
            cgr = tip[tj]

            if cgr == '0':
                owa[tj] += tiw / tigm1
            elif cgr == '1':
                owa[tj] += tiwm1 / tigm1

    towp = [owa[ti] / tgl[ti] for ti in range(tmn)]
    oowa = map(lambda x: sum(map(lambda y: 0. if x[y] == '.' else towp[y], range(tmn))), tpl)
    toowp = [oowa[ti] / tgl[ti] for ti in range(tmn)]
    
    print 'Case #{0}:'.format(tcn)

    for ti in range(tmn):
        print .25 * twp[ti] + 0.5 * towp[ti] + 0.25 * toowp[ti]
