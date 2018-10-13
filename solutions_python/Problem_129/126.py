def process_benefit(p1, p2, points, N):
    if p1[2] == p2[2]:
        temp = p1[0]
        p1[0] = p2[0]
        p2[0] = temp
    elif p1[2] > p2[2]:
        p1[2] -= p2[2]
        points += [[p2[0], p1[1], p2[2]]]
        p2[0] = p1[0]
    else:
        points += [[p1[0], p2[1], p1[2]]]
        p2[2] -= p1[2]
        p1[0] = p2[0]
    points.sort(key=lambda x: x[0]*N + x[1])


def calc_benefit(N, p1, p2):\
    # TODO: optimize it
    temp = float(p2[0] - p1[0]) / 2
    ans = (2*(N - p1[1]) + p2[0] + p1[0]) * temp
    ans -= (2*(N - p2[1]) + p2[0] + p1[0]) * temp
    return int(ans) * min(p1[2], p2[2])


def calc_ans(N, points):
    points.sort(key=lambda x: x[0]*N + x[1])
    ans = 0

    while len(points) > 1:
        cur_point = points[0]
        length = len(points)
        best_benefit = 0
        pair = None

        for x in xrange(1, length):
            point = points[x]
            if point[0] > cur_point[1]:
                break
            if point[1] > cur_point[1]:
                benefit = calc_benefit(N, cur_point, point)
                if benefit > best_benefit:
                    best_benefit = benefit
                    pair = point

        if pair is None:
            points = points[1:]
            continue

        ans += best_benefit
        process_benefit(cur_point, pair, points, N)

    return ans % 1000002013


def main():
    filename = 'input_a.in'
    filename_out = 'output_a.txt'
    result_lines = []
    with open(filename, 'r') as input_file:
        t = int(input_file.readline())
        for test_case in xrange(1, t + 1):
            [N, M] = [int(x) for x in input_file.readline().split()]
            points = []
            for _ in xrange(M):
                points += [[int(x) for x in input_file.readline().split()]]
            ans = calc_ans(N, points)
            line = 'Case #' + str(test_case) + ': ' + str(ans) + '\n'
            result_lines += [line]
    with open(filename_out, 'w') as output_file:
        output_file.writelines(result_lines)


main()