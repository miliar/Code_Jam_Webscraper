# This code only works under constraints for small dataset
def sub(i, exch, acts, occ):
    if i == len(acts)-1:
        return exch
    if acts[i][2] != acts[i+1][2]:
        return sub(i+1, exch+1, acts, occ)
    if acts[i+1][0] == acts[i][1]:
        return sub(i+1, exch, acts, occ)
    a = sub(i+1, exch+2, acts, occ)
    r = acts[i+1][0] - acts[i][1]
    if occ[acts[i][2]] + r <= 720:
        occ = occ[:]
        occ[acts[i][2]] += r
        b = sub(i+1, exch, acts, occ)
        return min(a, b)
    else:
        return a


def solve(acts, occ):
    acts = sorted(acts)
    acts.append((acts[0][0]+24*60,acts[0][0]+24*60, acts[0][2])) # guard
    return sub(0, 0, acts, occ)

for case in range(1, int(input())+1):
    ac, aj = map(int, input().split())
    acts = []
    C = 0
    for _ in range(ac):
        s, e = map(int, input().split())
        acts.append((s, e, 0))
        C += e-s
    J = 0
    for _ in range(aj):
        s, e = map(int, input().split())
        acts.append((s, e, 1))
        J += e-s
    answer = solve(acts, [C, J])
    print('Case #{}: {}'.format(case, answer))
