import operator
import functools
import sys


def get_optimal_prob(ps, u, k):
    """Get the optimal probability."""

    ps.sort()
    min_p = ps[0]
    devs = [min_p - i for i in ps]

    coeff = 0
    total_dev = 0
    base = None
    end = None
    for i, v in enumerate(devs):
        coeff += 1
        total_dev += v
        curr_base = (u - total_dev) / coeff
        curr = curr_base + v
        if curr >= 0:
            base = curr_base
        else:
            end = i
            break
    else:
        end = len(devs)

    assert base is not None
    for i in range(end):
        ps[i] += base + devs[i]

    return functools.reduce(operator.mul, ps)


def main():
    """The main driver."""
    with open(sys.argv[1], 'r') as inp:
        n_tests = int(inp.readline())
        for test_idx in range(n_tests):
            n, k = [int(i) for i in inp.readline().split()]
            u = float(inp.readline())
            ps = [float(i) for i in inp.readline().split()]
            # assert n == k
            assert len(ps) == n
            print('Case #{}: {}'.format(
                test_idx + 1,
                get_optimal_prob(ps, u, k)
            ))
            continue


if __name__ == '__main__':
    main()
