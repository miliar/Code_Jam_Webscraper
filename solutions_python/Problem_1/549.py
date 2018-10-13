import sys
import pprint

if len(sys.argv) > 1:
    debug = True
else:
    debug = False

f = open('A-small.in', 'r')
N = int(f.readline())
fo = open('A-small.out', 'w')
for n in range(N):
    S = int(f.readline())
    se = {}
    qs = []
    oqs = []
    for _ in range(S):
        se[f.readline().strip()] = 0
    Q = int(f.readline())
    rank = 0
    last_q = ''
    for _ in range(Q):
        rank += 1
        q = f.readline().strip()
        if last_q == '' or last_q != q:
            se[q] += 1
            qs.append(q)
            oqs.append(q.replace('Googol ','')[:2])
        last_q = q
    switches = 0
    mini = 0
    last_cut = []
    while True:
        b_dict = dict(map(lambda item: (item[1],item[0]),se.items()))
        try:
            mini = min(b_dict.keys())
            if mini == 0:
                raise ValueError
        except ValueError:
            # we found it
            break
        found_seq = False
        i = 0
        minors = {}
        max_min_rank = make_better = 0
        for q in qs:
            i += 1
            if not q in last_cut:
            #    print make_better, last_cut
                make_better = i
                last_cut.append(q)
        
        if max_min_rank < make_better:
            max_min_rank = make_better

        if max_min_rank <= 1:
            if debug:
                print make_better, last_cut
                pp = pprint.PrettyPrinter()
                pp.pprint(max_min_rank)
                pp.pprint(mini)
                pp.pprint(se)
                pp.pprint(qs)
                pp.pprint(oqs)
                print '\n'
            pass
        else:
            last_cut = []
            for rem in qs[:max_min_rank-1]:
                se[rem] -= 1
            del qs[:max_min_rank-1]
            switches += 1

    res = "Case #" + str(n+1) + ": " + str(switches) + '\n'
    fo.write(res)
    if debug: print S, Q, res,
