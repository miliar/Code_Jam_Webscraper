from __future__ import print_function

read_floats = lambda: map(float, raw_input().split())


def solve():
    n = raw_input()
    naomi = sorted(read_floats())
    ken = sorted(read_floats())

    def honest_war(nao, ken):
        kg = iter(ken)
        for i, n in enumerate(nao):
            if not any(n < k for k in kg):
                return len(nao) - i
        return 0

    def deceitful_war(nao, ken):
        ng = iter(nao)
        for i, k in enumerate(ken):
            if not any(n > k for n in ng):
                return i
        return len(nao)

    honest_w = honest_war(naomi, ken)
    deceitful_w = deceitful_war(naomi, ken)
    return deceitful_w, honest_w


def main():
    T = int(raw_input())
    for case in xrange(1, T+1):
        dw, hw = solve()
        print("Case #%d: %d %d" % (case, dw, hw))

if __name__ == '__main__':
    main()
