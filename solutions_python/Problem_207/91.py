# https://code.google.com/codejam/contest/8294486/dashboard

import itertools

def solve(r, y, b):
    n = r + y + b
    if any(x > n // 2 for x in (r, y, b)):
        return None
    pool = [('R', r), ('Y', y), ('B', b)]
    pool.sort(key=lambda x: -x[1])
    l1 = [pool[0][0] + pool[1][0]] * pool[1][1] + [pool[0][0] + pool[2][0]] * (pool[0][1] - pool[1][1])
    l3 = [pool[2][0]] * (pool[2][1] - (pool[0][1] - pool[1][1]))
    ans = [x for x in itertools.chain.from_iterable(itertools.zip_longest(l1, l3)) if x]
    return ''.join(ans)

if __name__ == "__main__":
    filein = open('20171BB.in', 'r')
    fileout = open('20171BB.out', 'w')
    T = int(filein.readline())
    for t in range(T):
        fileout.write('Case #%d: ' % (t + 1))
        [N, R, O, Y, G, B, V] = map(int, filein.readline().split())

        R_, Y_, B_ = R - G, Y - V, B - O
        ans = solve(R_, Y_, B_)
        if ans is None:
            ans = 'IMPOSSIBLE'
        else:
            ans_list = list(ans)
            substitutions = []
            if G != 0:
                substitutions.append(('R', 'R' + 'GR' * G))
            if V != 0:
                substitutions.append(('Y', 'Y' + 'YV' * V))
            if O != 0:
                substitutions.append(('B', 'B' + 'BO' * O))
            for target, goal in substitutions:
                try:
                    i = next(i for i, x in enumerate(ans_list) if x == 'R')
                    ans_list[i] = goal
                except StopIteration:
                    ans_list.append(goal[1:])
            ans = ''.join(ans_list)
        fileout.write(ans + '\n')

    filein.close()
    fileout.close()
