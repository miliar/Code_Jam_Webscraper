#!/usr/bin/env python3


def calc_free(bathroom):
    s = []
    counter = 0
    for stall in bathroom:
        if stall == 1:
            s.append(-1)
            counter = 0
        elif stall == 0:
            s.append(counter)
            counter += 1
    return s


def find_spot(n, k):
    bathroom = [1] + (n * [0]) + [1]
    min_g, max_g = 0, 0
    for person in range(0, k):

        l_s = calc_free(bathroom)
        r_s = list(reversed(calc_free(reversed(bathroom))))

        m_min = None
        p_min = None
        distinct_min = True
        valid_pos = []
        for l, r, pos in zip(l_s, r_s, range(0, n+2)):
            minimum = min(l, r)
            if minimum == -1:
                continue
            if m_min is None or m_min < minimum:
                m_min = minimum
                p_min = pos
                distinct_min = True
                valid_pos = [pos]
            elif m_min is not None and m_min == minimum:
                distinct_min = False
                valid_pos.append(pos)

        m_max = None
        p_max = None
        distinct_max = True
        for l, r, pos in zip(l_s, r_s, range(0, n+2)):
            maximum = max(l, r)
            if maximum == -1 or pos not in valid_pos:
                continue
            if m_max is None or m_max < maximum:
                m_max = maximum
                p_max = pos
                distinct_max = True
            elif m_max is not None and m_max == maximum:
                distinct_max = False

        min_g = m_min
        max_g = m_max

        if distinct_min:
            bathroom[p_min] = 1
        elif distinct_max:
            bathroom[p_max] = 1
        else:
            if p_max:
                bathroom[p_max] = 1
            else:
                bathroom[p_min] = 1

    return "{} {}".format(max_g, min_g)



if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        n, k = input().rstrip().split()
        print("Case #{0}: {1}".format(i, find_spot(int(n), int(k))))
