def answer(cds, jks):
    total_minutes = 24 * 60

    times = []
    for c, d in cds:
        times.append((c, d, 1))
    for j, k in jks:
        times.append((j, k, -1))

    times.sort()
    n = len(times)

    total_diff = delta_diff = total_exchange = 0
    minus_options, plus_options = [], []
    for i in range(n):
        total_diff += times[i][2] * (times[i][1] - times[i][0])

        time_after_last = ((times[i][0] - times[i - 1][1] + total_minutes) % total_minutes)
        if times[i][2] == times[i - 1][2]:
            total_diff += times[i][2] * time_after_last

            if times[i][2] == 1:
                minus_options.append(2 * time_after_last)
            else:
                plus_options.append(2 * time_after_last)
        else:
            delta_diff += time_after_last
            total_exchange += 1

    lower_bound = total_diff - delta_diff
    upper_bound = total_diff + delta_diff

    minus_options.sort(reverse=True)
    for minus_option in minus_options:
        if lower_bound > 0:
            lower_bound -= minus_option
            total_exchange += 2
        else:
            break

    plus_options.sort(reverse=True)
    for plus_option in plus_options:
        if upper_bound < 0:
            upper_bound += plus_option
            total_exchange += 2
        else:
            break

    return total_exchange


def read_ints():
    return tuple(int(j) for j in input().split(" "))


def main():
    t = int(input())
    for i in range(1, t + 1):
        ac, aj = read_ints()
        cds = [read_ints() for j in range(ac)]
        jks = [read_ints() for j in range(aj)]

        result = answer(cds, jks)
        print("Case #{}: {}".format(i, result))


if __name__ == "__main__":
    main()
