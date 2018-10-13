t = int(raw_input())

for case in xrange(t):
    hd, ad, hk, ak, b, d = map(int, raw_input().split())

    result = 1 << 30

    nak = ak
    nhd = hd
    moves = 0
    for debuffs in xrange(101):
        if debuffs:
            if nhd - (nak - d) <= 0:
                nhd = hd - nak
                moves += 1
                if nhd - (nak - d) <= 0:
                    break
            nak = max(0, ak - debuffs * d)
            nhd -= nak
            moves += 1
        nad = ad
        nnhd = nhd
        nmoves = moves
        for buffs in xrange(101):
            if buffs:
                if nnhd - nak <= 0:
                    nnhd = hd - nak
                    nmoves += 1
                    if nnhd - nak <= 0:
                        break
                nad = ad + buffs * b
                nnhd -= nak
                nmoves += 1
            nhk = hk
            nnnhd = nnhd
            nnmoves = nmoves
            for attacks in xrange(1, 101):
                if nhk - nad <= 0:
                    result = min(result, nnmoves + 1)
                    break
                if nnnhd - nak <= 0:
                    nnnhd = hd - nak
                    nnmoves += 1
                    if nnnhd - nak <= 0:
                        break
                nhk -= nad
                nnnhd -= nak
                nnmoves += 1

    print 'Case #%d: %s' % (case + 1, result if result != 1 << 30 else 'IMPOSSIBLE')
