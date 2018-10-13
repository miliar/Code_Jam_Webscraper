import sys
import bisect


def answer(horses, distances):

    assert distances[-1] == -1

    del distances[-1]

    best_times = [0.0] * len(horses)

    partial_sums = [0.0]
    for item in distances:
        partial_sums.append(item+partial_sums[-1])



    for index, partial_dist in enumerate(partial_sums):
        if index == 0:
            continue
        cur_best_time = 1e15
        for j in range(index):
            max_dist, speed = horses[j]
            if max_dist >= partial_dist - partial_sums[j]:
                new_time = best_times[j] + (partial_dist - partial_sums[j] + 0.0) / (speed + 0.0)
                if new_time < cur_best_time:
                    cur_best_time = new_time
        if cur_best_time == 1e15:
            raise ValueError('{}{}'.format(horses, partial_sums))

        best_times[index] = cur_best_time

    return best_times[-1]


if __name__ == "__main__":

    T = int(sys.stdin.next())
    queries = []
    for i in range(T):
        N, Q = map(int, sys.stdin.next().split(' '))
        horses = []
        for j in range(N):
            max_dist, speed = map(int, sys.stdin.next().split(' '))
            horses.append((max_dist, speed))

        distances = []
        for k in range(N):
            all_dists = map(int, sys.stdin.next().split(' '))
            distances.append(max(all_dists))

        for l in range(Q):
            beg, end = map(int, sys.stdin.next().split(' '))

        queries.append((horses, distances))
    for i, q in enumerate(queries):
        #if answer3(*q) != answer2(*q):
        #    raise ValueError('Wrong answer on {}'.format(q))
        print "".join(["Case #", str(i+1), ": ", str(answer(*q))])
