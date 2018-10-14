IN = 'B-small-attempt0.in'
OUT = 'b.out'

with open(IN, 'r') as fin:
    with open(OUT, 'w') as fout:
        lines = fin.readlines()
        T = int(lines.pop(0))

        for case in xrange(1, T + 1):
            line = lines.pop(0)
            parts = line.split()

            C = int(parts.pop(0))
            cc = [parts.pop(0) for i in xrange(C)]
            combo = {}
            for c in cc:
                combo[c[:-1]] = c[-1]
                combo[c[-2::-1]] = c[-1]                     
            
            D = int(parts.pop(0))            
            dd = [parts.pop(0) for i in xrange(D)]
            oppo = {}
            for d in dd:
                if d[0] in oppo:
                    oppo[d[0]].add(d[1])
                oppo[d[0]] = set([d[1]])
                if d[1] in oppo:
                    oppo[d[1]].add(d[1])
                oppo[d[1]] = set([d[0]])

            N = int(parts.pop(0))
            invoke = parts.pop(0)

            assert len(parts) == 0

            P = lambda x: ord(x) - ord('A')

            LIST = []
            COUNTT = [0] * 26
            for element in invoke:
                LIST.append(element)
                COUNTT[P(element)] += 1
                if len(LIST) >= 2:
                    if ''.join(LIST[-2:]) in combo:
                        what = ''.join(LIST[-2:])
                        del LIST[-2:]
                        LIST.append(combo[what])
                        COUNTT[P(what[0])] -= 1
                        COUNTT[P(what[1])] -= 1
                    elif element in oppo:
                        for o in oppo[element]:
                            if COUNTT[P(o)] > 0:
                                LIST = []
                                COUNTT = [0] * 26

            print 'Case #%d: %s' % (case, '[' + ', '.join(LIST) + ']')
            fout.write('Case #%d: %s\n' % (case, '[' + ', '.join(LIST) + ']'))
