import math


def maxminlr(stalls_count, users_count):
    order = int(math.log(users_count, 2))
    pow_two = 2 ** order

    k, p = divmod(stalls_count, pow_two * 2)
    t = users_count

    if p in range(0, t - pow_two):
        return (k - 1, k - 1)
    elif p in range(t - pow_two, t):
        return (k, k - 1)
    elif p in range(t, pow_two * 2):
        return (k, k)


def main():
    tests_count = int(input())

    for i in range(1, tests_count + 1):
        stalls_count, users_count = input().split()
        maxlr, minlr = maxminlr(int(stalls_count), int(users_count))
        print('Case #{}: {} {}'.format(i, maxlr, minlr))

if __name__ == "__main__":
    main()
