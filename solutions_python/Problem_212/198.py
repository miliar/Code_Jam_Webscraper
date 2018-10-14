import math


def splitAndList(inp):
    ret = []
    s = inp.split(' ')

    for i in range(len(s)):
        ret.append(int(s[i]))

    return ret


def splitAndDict(f, inp):
    ret = {}
    s = inp.split(' ')
    s2 = f.split(' ')

    for i in range(len(s)):
        ret[s2[i]] = int(s[i])

    return ret

def c2(group, t):

    group = list(group)

    for p in t:
        if p not in group:
            return False

        group.remove(p)

    return True

def pick(group, last, p):

    best = (p - last) % p

    if best in group:
        return best

    if 2 == p:
        return 1

    if 3 == p:
        return group[0]

    if 4 == p:
        if 1 in group and 3 in group:
            return 1

        if 2 in group:
            return 2

        return group[0]


def solve(pr):
    n = pr['n']
    p = pr['p']
    g = list((p - (g % p)) % p for g in pr['g'])
    g = sorted(g)

    ret = 0
    last = 0

    while 0 != len(g):

        if last == 0:
            ret += 1

        next = pick(g, last, p)
        last = (last + next) % p
        g.remove(next)

    return ret

def main():
    probs = []

    for i in range(int(raw_input())):
        prob = splitAndDict("n p", raw_input())

        prob['g'] = splitAndList(raw_input())

        probs.append(prob)

    count = 0
    for prob in probs:
        count += 1
        ret = solve(prob)

        print("Case #{}: {}".format(count, ret))


if __name__ == "__main__":
    main()