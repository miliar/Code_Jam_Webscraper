import re
import itertools

def better(n1, n2, better_n1, better_n2):
    diff = abs(n1 - n2) - abs(better_n1 - better_n2)
    if diff > 0:
        return True
    elif diff == 0:
        return (better_n1, better_n2) < (n1, n2)
    return False

def solve(n1, n2):
    best_n1, best_n2 = 10e18, 10e19
    
    quest1_pos = [m.start() for m in re.finditer(r'\?', n1)]
    quest2_pos = [m.start() for m in re.finditer(r'\?', n2)]

    for pos1 in itertools.product(range(10), repeat=len(quest1_pos)):
        s1 = list(n1)
        for i, p in zip(quest1_pos, pos1):
            s1[i] = str(p)
        s1 = int(''.join(s1))
        for pos2 in itertools.product(range(10), repeat=len(quest2_pos)):
            s2 = list(n2)
            for i, p in zip(quest2_pos, pos2):
                s2[i] = str(p)
            s2 = int(''.join(s2))

            if better(best_n1, best_n2, s1, s2):
                best_n1, best_n2 = s1, s2

    return best_n1, best_n2

T = int(raw_input())

for case in xrange(1, T + 1):
    n1, n2 = raw_input().split()
    best_n1, best_n2 = solve(n1, n2)
    print 'Case #{}: {} {}'.format(
        case,
        str(best_n1).rjust(len(n1), '0'),
        str(best_n2).rjust(len(n2), '0'))
