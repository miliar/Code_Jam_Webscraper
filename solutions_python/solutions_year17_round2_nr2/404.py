import operator

color_code = {'r':1, 'y': 2, 'b': 4, 'o': 3, 'g': 6, 'v': 5}


def is_not_same_color(color_a, color_b):
    return color_code[color_a] & color_code[color_b] == 0


def back(n, color_counter, tail):
    if n == 0:
        if is_not_same_color(tail[0], tail[-1]):
            return tail
        return None
    max_color, max_v = None, -1

    for k in color_counter.keys():
        if color_counter[k] == 0:
            continue
        if color_counter[k] >= max_v and (len(tail) == 0 or is_not_same_color(tail[-1], k)):
            max_color = k
            max_v = color_counter[k]

    # sorted_color_counter = sorted(color_counter.items(), key=operator.itemgetter(1))
    if max_color is None or (len(tail) > 0 and max_color == tail[-1]):
        return None
    color_counter[max_color] -= 1
    return back(n - 1, color_counter, tail + [max_color])


def solve(n, r, o, y, g, b, v):
    count = {}
    count['r'] = r
    count['o'] = o
    count['y'] = y
    count['g'] = g
    count['b'] = b
    count['v'] = v

    sorted_count = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
    stalls = [None] * n

    maximum_color = sorted_count[0][0]

    if count[maximum_color] * 2 > n:
        return None

    for i in range(count[maximum_color]):
        stalls[i * 2] = maximum_color

    if sorted_count[0][1] * 2 > n:
        return None

    second_color = sorted_count[1][0]
    third_color = sorted_count[2][0]
    current_color = second_color

    for i in range(count[maximum_color], (n + 1) / 2):
        stalls[i * 2] = second_color
        count[second_color] -= 1

    for i in range(n):
        if stalls[i] is None:
            if count[second_color] > 0:
                stalls[i] = second_color
                count[second_color] -= 1
            else:
                stalls[i] = third_color
    return stalls


for t in range(1, int(raw_input()) + 1):
    n, r, o, y, g, b, v = map(int, raw_input().split())
    answer = solve(n, r, o, y, g, b, v)
    print 'Case #%d: %s' % (t, ''.join(answer).upper() if answer is not None else "IMPOSSIBLE")
