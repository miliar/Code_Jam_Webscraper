import os


def compute_d(row):
    distances = {}
    for j in range(1, n + 1):
        if empty[j]:
            left, cur = 0, j
            while cur != 1:
                cur -= 1
                if row[cur]:
                    left += 1
                else:
                    break

            right, cur = 0, j
            while cur != n:
                cur += 1
                if row[cur]:
                    right += 1
                else:
                    break

            distances[j] = (left, right)
    return distances


if __name__ == '__main__':
    input_path = os.path.join(os.getcwd(), 'C-small-1-attempt0.in')
    output_path = os.path.join(os.getcwd(), 'C-small-1-attempt0.out')

    with open(input_path, 'r') as f_in:
        with open(output_path, 'w') as f_out:
            t = int(f_in.readline())
            for x in range(1, t + 1):
                n, k = map(int, f_in.readline().split())
                empty = [False, *([True] * n), False]

                for i in range(k):
                    d = compute_d(empty)

                    max_min_stall = max(d, key=lambda key: min(d[key]))
                    max_min_distance = min(d[max_min_stall])
                    candidates = list(filter(lambda key: min(d[key]) == max_min_distance, d))

                    if len(candidates) == 1:
                        result = candidates[0]
                    else:
                        max_max_stall = max(candidates, key=lambda key: max(d[key]))
                        max_max_distance = max(d[max_max_stall])
                        candidates = list(filter(lambda key: max(d[key]) == max_max_distance, candidates))

                        if len(candidates) == 1:
                            result = candidates[0]
                        else:
                            result = min(candidates)

                    empty[result] = False

                f_out.write('Case #{x}: {y} {z}'.format(x=x, y=max(d[result]), z=min(d[result])))
                f_out.write('\n')

        print('Finished')
