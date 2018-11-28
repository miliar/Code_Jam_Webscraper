def solve(k, cakes):
    from math import pi
    value_r = list(tuple(map(lambda elem: elem[0] ** 2 * pi, cakes)))
    value_h = list(tuple(map(lambda elem: elem[1] * 2 * elem[0] * pi, cakes)))
    from itertools import combinations
    max_value = 0
    for l in combinations(range(len(cakes)), k):
        max_value = max(max_value, max(map(lambda i: value_r[i], l)) + sum(map(lambda i: value_h[i], l)))
    return max_value


def main():
    input_file_name = 'A-input.in'
    output_file_name = 'A-output.out'
    with open(input_file_name) as fin:
        with open(output_file_name, 'w') as fout:
            t = int(fin.readline())
            for tc in range(t):
                n, k = tuple(map(int, fin.readline().split()))
                cake = []
                for i in range(n):
                    cake.append(tuple(map(int, fin.readline().split())))

                fout.write("Case #%d: %f\n" % ((tc + 1), solve(k, cake)))
main()