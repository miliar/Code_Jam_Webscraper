T = int(raw_input().strip())

I, J, K = 2, 3, 4


def sign(x):
    if x < 0:
        return -1
    else:
        return 1

PROD = [
    [1, I, J, K],
    [I, -1, K, -J],
    [J, -K, -1, I],
    [K, J, -I, -1]]


def quat(a, b):
    return PROD[a - 1][b - 1]


def translate(inp):
    if inp == "i":
        return I
    elif inp == "j":
        return J
    else:
        return K


for i in xrange(T):
    L, X = map(int, raw_input().strip().split(' '))
    lis = list(raw_input().strip())
    lis = [translate(li) for li in lis]
    lx = L * X
    if lx < 3:
        print "Case #%s: %s" % (i + 1, "NO")
        continue
    front = [1 for _ in xrange(lx)]
    back = [1 for _ in xrange(lx)]
    front[0] = lis[0]
    back[-1] = lis[-1]
    i_good, k_good = set(), set()
    if front[0] == I:
        i_good.add(0)
    if back[-1] == K:
        k_good.add(lx - 1)

    for j in xrange(1, lx):
        front[j] = sign(front[j - 1]) * quat(abs(front[j - 1]), lis[j % L])
        if front[j] == I:
            i_good.add(j)

    for j in xrange(lx - 2, -1, -1):
        back[j] = sign(back[j + 1]) * quat(lis[j % L], abs(back[j + 1]))
        if back[j] == K:
            k_good.add(j)

    i_good = sorted(i_good)
    il = len(i_good)
    i_index = 0
    k_good = sorted(k_good)
    kl = len(k_good)
    k_index = 0

    if il == 0 or kl == 0:
        print "Case #%s: %s" % (i + 1, "NO")
        continue

    while k_index < kl and i_good[i_index] + 1 >= k_good[k_index]:
        k_index += 1

    if k_index == kl:
        print "Case #%s: %s" % (i + 1, "NO")
        continue

    found = False
    while k_index < kl and i_index < il:
        if back[i_good[i_index] + 1] == I:
            found = True
            break
        i_index += 1
        if i_index == il:
            break
        while k_index < kl and i_good[i_index] + 1 >= k_good[k_index]:
            k_index += 1
    if found:
        print "Case #%s: %s" % (i + 1, "YES")
    else:
        print "Case #%s: %s" % (i + 1, "NO")
