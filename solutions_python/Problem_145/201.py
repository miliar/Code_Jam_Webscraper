import pp
import sys

def gcd(a, b):
    return b if a == 0 else gcd(b % a, a)
def lcm(a, b):
    return (a * b) / gcd(a,b)

def calc(a, b):
    z = lcm(a[1], b[1])
    an = (z // a[1]) * a[0] + (z // b[1]) * b[0]
    bn = z * 2
    g = gcd(an,bn)

    return (an//g, bn/g)

def solve2():
    a = [(0, 1), (1, 1)]
    gen = [-1, 0]
    i = 1
    while i < len(a):
        if gen[i] == 5:
            break
        for j in xrange(0, i):
            new_gen = calc(a[i], a[j])
            if new_gen not in a:
                print a[i],a[j],new_gen
                a.append(new_gen)
                gen.append(-1 if gen[i] == -1 and gen[j] == -1 else min(41 if gen[i] == -1 else gen[i], 41 if gen[j] == -1 else gen[j]) + 1)
            else:
                for p in xrange(len(a)):
                    if new_gen == a[p]:
                        break

                k = -1 if gen[i] == -1 and gen[j] == -1 else min(41 if gen[i] == -1 else gen[i], 41 if gen[j] == -1 else gen[j]) + 1
                gen[p] = min(gen[p],k)
                print a[i],a[j],new_gen,k

        i += 1
    d = {}
    for i in xrange(len(a)):

        if a[i][1] not in d:
            d[a[i][1]] = []
        d[a[i][1]].append(gen[i])

    for item in d:
        print item, list(sorted(d[item]))

def solve(a, b):
    g = gcd(a,b)
    a /= g
    b /= g

    p = 1
    k = 0
    while p < b:
        p *= 2
        k += 1

    if p != b or a < 1 or a > b:
        return 'impossible'

    if a == 1:
        return str(k)

    a = (a - 1) // 2
    r = (1 << (k - 1)) - 1
    step = 1 << (k - 2)
    result = 1
    while step > 0:
        if a > r - step:
            return str(result)
        r -= step
        step >>= 1
        result += 1

    return 'impossible'

a = [(0, 1), (1, 1)]
gen = [-1, 0]
def solve3():
    i = 1
    while i < len(a):
        if gen[i] == 10:
            break
        for j in xrange(0, i):
            new_gen = calc(a[i], a[j])
            if new_gen not in a:
                a.append(new_gen)
                gen.append(-1 if gen[i] == -1 and gen[j] == -1 else min(41 if gen[i] == -1 else gen[i], 41 if gen[j] == -1 else gen[j]) + 1)
            else:
                for p in xrange(len(a)):
                    if new_gen == a[p]:
                        break

                k = -1 if gen[i] == -1 and gen[j] == -1 else min(41 if gen[i] == -1 else gen[i], 41 if gen[j] == -1 else gen[j]) + 1
                gen[p] = min(gen[p],k)
        i += 1

def solve_small(a, gen, p, q):
    new_gen = (p, q)
    for i in xrange(len(a)):
        if new_gen == a[i]:
            return str(gen[i])

    return 'impossible'

job_server = pp.Server()

f = open('A-large.in', 'r')
T = int(f.readline()) + 1

jobs = []
for test in xrange(1, T):
    p, q = map(int, f.readline().split('/'))

    jobs.append(job_server.submit(solve,(p, q), (gcd,)))

f.close()

open('output.txt', 'w').write('\n'.join(['Case #%d: %s' % (i + 1, str(job())) for i, job in enumerate(jobs)]))
