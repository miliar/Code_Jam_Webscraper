def solve(horse_details, distances, start, end):
    min_time = [100000000000.0 for _ in range(len(horse_details))]

    min_time[start] = 0.0
    for i in range(start, len(horse_details)):
        current_tm = min_time[i]
        if i == end:
            return current_tm
        mx_dist, spd = horse_details[i]
        dist_cov = 0
        for j in range(i + 1, len(horse_details)):
            dist_cov += distances[j - 1]
            if dist_cov > mx_dist:
                break
            min_time[j] = min(min_time[j], current_tm + dist_cov / spd)


def get_input():
    n, q = map(int, input().split())
    horse_details = [tuple(map(int, input().split()))
                     for _ in range(n)]
    adj_mat = [list(map(int, input().split()))
               for _ in range(n)]
    start, end = map(int, input().split())
    distances = [adj_mat[i][i + 1]
                 for i in range(n - 1)]
    return horse_details, distances, start, end


def main():
    t_case = int(input())
    for i in range(t_case):
        horse_details, distances, start, end = get_input()
        print("Case #{}: {}".format(i + 1,
                                    solve(horse_details, distances,
                                          start - 1,
                                          end - 1)))
    pass


if __name__ == "__main__":
    import sys

    sys.stdin = open("C-small-attempt0.in", "r")
    sys.stdout = open("out", "w")
    main()
