import sys


def actual_war(naomis, kens_orig):
    kens = kens_orig[:]
    s = 0
    for n in naomis:
        if n > kens[0]:
            k = kens.pop(-1)
        else:
            for i, k in reversed(list(enumerate(kens))):
                if k > n:
                    break
            k = kens.pop(i)
        s += int(n > k)
    return s


def deceitful_war(naomis, kens):
    if len(naomis) == 0:
        return 0
    if naomis[0] > kens[0]:
        return 1 + deceitful_war(naomis[1:], kens[1:])
    else:
        if len(naomis) == 1:
            return int(naomis[0] > kens[0])
        else:
            naomis_selection = naomis[-1]
            kens_selection = kens[0]
            return (int(naomis_selection > kens_selection) +
                    deceitful_war(naomis[:-1], kens[1:]))


def main():
    ifile = sys.stdin
    ofile = sys.stdout
    for test_number in xrange(1, int(ifile.readline().strip()) + 1):
        int(ifile.readline().strip())  # number of weights, not asserting.
        naomis_weights = sorted(map(float, ifile.readline().strip().split()),
                                reverse=True)
        kens_weights = sorted(map(float, ifile.readline().strip().split()),
                              reverse=True)
        ofile.write("Case #%d: %d %d\n" % (
            test_number, deceitful_war(naomis_weights, kens_weights),
            actual_war(naomis_weights, kens_weights)))


if __name__ == "__main__":
    main()
