#!/usr/bin/env sage

def gen(P):
    a = [[P if i == j else 0 for j in range(P)] for i in range(1, P)]
    for x in range(1, P**P):
        c = [x // P ** i % P for i in range(P)]
        if sum(i * c[i] for i in range(P)) % P == 0:
            a.append(c)
    for t in a:
        good = True
        for s in a:
            if s != t and sum([1 for i in range(P) if t[i] >= s[i]]) == P:
                good = False
                break
        if good:
            yield t


u = {p : list(gen(p)) for p in range(2, 5)}

def solve(b, P):
    p = MixedIntegerLinearProgram(maximization=True, solver = "coin")
    x = p.new_variable(integer=True, nonnegative=True)
    v = u[P]
    n = len(v)
    for i in range(P):
        p.add_constraint(sum(x[j] * v[j][i] for j in range(n)) <= b[i])
    p.set_objective(sum(x[j] for j in range(n)))
    return round(p.solve())

T = input()

for ti in range(1, T+1):
    N, P = map(int, raw_input().split())
    G = list(map(lambda s : int(s) % P, raw_input().split()))
    b = [G.count(i) for i in range(P)]
    a = solve(b, P)
    for i in range(P):
        if b[i]:
            b[i] -= 1
            a = max(a, solve(b, P) + 1)
            b[i] += 1
    print "Case #%d: %d" %(ti, a)
 
