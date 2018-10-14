from collections import Counter, defaultdict

input_file = 'B-small-attempt0.in'
output_file = 'B.out'

with open(input_file) as f:
    with open(output_file, 'w') as out:
        cases = f.readline()
        cases = int(cases)
        for i in xrange(1, cases+1):
            n, c, m = map(int, f.readline().split())
            buys = [defaultdict(int) for jj in range(n+1)]
            # try:
            for j in range(m):
                x = f.readline().split()
                p, b = map(int, x)
                buys[p][b] = 1 + buys[p][b]
            # except Exception as e:
            #     print n, c, m, len(buys)
            end_b = [sum(pp.values()) for pp in buys]
            bb = [[k, bb] for k, bb in enumerate([] + [sorted(map(list, bb.items()), key=lambda x: x[1]) for bb in buys]) if bb]
            # print bb
            rides = 0
            while bb:
                rides += 1
                ride_clients = set()
                to_remove = []
                for ii in xrange(len(bb)):
                    # bb[ii] = [pos, [[client, times]]]
                    buys = bb[ii][1]
                    new_buys = []
                    for c, t in buys:
                        if c not in ride_clients and len(ride_clients) < bb[ii][0]:
                            ride_clients.add(c)
                            t -= 1
                        if t:
                            new_buys.append([c, t])
                    if new_buys:
                        new_buys.sort(key=lambda x: x[1])
                        bb[ii][1] = new_buys
                    else:
                        to_remove.append(ii)
                for rr in reversed(to_remove):
                    bb.pop(rr)
            proms = sum([max(ee - rides, 0) for ee in end_b])
            ans = '{} {}'.format(rides, proms)
            print 'Case #{i}: {res}'.format(res=ans, i=i)
            out.write('Case #{i}: {res}\n'.format(res=ans, i=i))