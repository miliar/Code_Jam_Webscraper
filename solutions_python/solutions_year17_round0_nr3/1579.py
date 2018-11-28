
def simulate(N, K):
    taken = [-1, N]
    best = None
    for _ in range(K):
        maximal_closest = -1
        l_most_i = 0
        for st in range(N):
            if st == taken[l_most_i + 1]:
                l_most_i += 1
                if l_most_i == len(taken) - 1:
                    break
                continue
            ls = st - taken[l_most_i] - 1
            rs = taken[l_most_i + 1] - st - 1
            m = min(ls, rs)
            if m > maximal_closest:
                maximal_closest = m
                best = (st, ls, rs)
            elif m == maximal_closest:
                if max(ls, rs) > max(best[1], best[2]):
                    best = (st, ls, rs)
                # If they're equal the leftmost wins
        taken = sorted(taken + [best[0]])
    return best[1:]


def main():
    T = int(input())
    for case in range(1, T + 1):
        N, K = map(int, input().split())
        ls, rs = simulate(N, K)
        print("Case #{}: {} {}".format(case, max(ls, rs), min(ls, rs)))

if __name__ == '__main__':
    main()
