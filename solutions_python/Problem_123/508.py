from math import sqrt

def osmos(a, motes):
    if not motes:
        return 0

    b = a
    motes = sorted(motes)
    output = 0
    i = 0
    while i < len(motes) and motes[i] < b:
        b += motes[i]
        i += 1

    if i == len(motes):
        return 0
    if b == 1:
        return 1+osmos(b,motes[i:-1])
    return min(1 + osmos(b, [b-1] + motes[i:]), 1 + osmos(b, motes[i:-1]))


def solve(f):
    an = f.readline().split()
    a = long(an[0])
    n = long(an[1])

    motes = sorted(map(int, f.readline().split()))

    return osmos(a, motes)



if __name__ == "__main__":
    solve()