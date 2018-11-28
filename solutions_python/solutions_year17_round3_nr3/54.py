import operator
import functools


def get_product(v):
    return functools.reduce(operator.mul, v, 1)


def answer(k, u, ps):
    n = len(ps)
    ps.sort()

    for i in range(n, 0, -1):
        new_p = (sum(ps[:i]) + u) / i
        if new_p >= ps[i - 1]:
            return new_p ** i * get_product(ps[i:])

    return -1


def read_ints():
    return tuple(int(j) for j in input().split(" "))


def read_floats():
    return list(float(j) for j in input().split(" "))


def main():
    t = int(input())
    for i in range(1, t + 1):
        n, k = read_ints()
        u, = read_floats()
        ps = read_floats()

        result = answer(k, u, ps)
        print("Case #{}: {:.8f}".format(i, result))


if __name__ == "__main__":
    main()
