import bisect


def play_war(naomis, kens):
    res = 0
    for n in naomis:
        i = bisect.bisect(kens, n)
        if i != len(kens):
            kens.pop(i)
        else:
            res += 1

    return res


def play_deceitful_war(naomis, kens):
    acc = []
    for i, n in enumerate(naomis):
        pos = bisect.bisect_right(kens, n)
        acc.append((i, pos))

    offset, res = 0, 0
    for i, pos in acc:
        if (offset == -1 or pos >= offset) and naomis[i] > kens[offset]:
            offset += 1
            res += 1

    return res



def solve(naomis, kens):
    naomis.sort()
    kens.sort()
    return (play_deceitful_war(naomis[:], kens[:]),
            play_war(naomis[:], kens[:]))


if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(t):
        n = int(raw_input())
        naomis = map(float, raw_input().split())
        kens = map(float, raw_input().split())
        print("Case #{0}: {1} {2}".format(i + 1, *solve(naomis, kens)))
