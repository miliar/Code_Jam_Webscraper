import math


def dadd(d, k, v):
    if k in d:
        d[k] += v
    else:
        d[k] = v


def unset_high_bit(n):
    i = 1
    while i <= n:
        i <<= 1
    return n ^ (i >> 1)


def print_case(case_num, s1, s2):
    print("Case #{0}: {1} {2}".format(case_num, max(s1, s2), min(s1, s2)))


def main():
    t = int(input())

    for case in range(t):
        n, k = [int(x) for x in input().strip().split()]

        section = int(math.log(k, 2)) + 1
        spans = {n: 1}
        for s in range(section):
            new_spans = dict()
            for value, count in spans.items():
                value -= 1
                half = value // 2
                if value % 2 == 0:
                    dadd(new_spans, half, 2 * count)
                else:
                    dadd(new_spans, half, count)
                    dadd(new_spans, half + 1, count)
            spans = new_spans

        k = unset_high_bit(k) + 1
        if len(spans) == 1:
            low = high = spans.popitem()
        else:
            low, high = spans.items()
        if low[1] > high[1]:
            low, high = high, low

        if low[1] == high[1]:
            print_case(case+1, high[0], low[0])
        else:
            diff = (low[1] + high[1]) // 2 - low[1]
            if high[0] > low[0]:
                if k <= diff:
                    print_case(case + 1, high[0], high[0])
                else:
                    print_case(case + 1, high[0], low[0])
            else:
                if k <= low[1]:
                    print_case(case + 1, high[0], low[0])
                else:
                    print_case(case + 1, high[0], high[0])


            # brute force
            #
            # sizes = [n]
            # for person in range(k):
            #     m = max(sizes)
            #     sizes.remove(m)
            #     m -= 1
            #     half1 = m // 2
            #     half2 = half1 + (m % 2)
            #     sizes.append(half1)
            #     sizes.append(half2)
            # else:
            #     print("Case #{0}: {1} {2}".format(case+1, half2, half1))

if __name__ == '__main__':
    main()
