def get_last_lsrs(n, k):
    stalls = [1] + ([0] * n) + [1]

    for someone in range(0, k):
        (choosen_start, choosen_end) = (0, 0)
        (empty_start, empty_end) = (0, 0)

        for stall_i in range(0, len(stalls)):
            if empty_start == 0 and stalls[stall_i] == 0:
                empty_start = stall_i

            if empty_start != 0 and stalls[stall_i + 1] != 0:
                empty_end = stall_i
                size = empty_end - empty_start

                if (choosen_end - choosen_start) < size:
                    choosen_start = empty_start
                    choosen_end = empty_end
                empty_start = 0

        chosen_i = int((choosen_start + choosen_end) / 2)
        stalls[chosen_i] = 1

    ls = chosen_i - choosen_start
    rs = choosen_end - chosen_i
    return (max(ls, rs), min(ls, rs))


t = int(input())
for case in range(1, t + 1):
    (n, k) = map(int, input().split())
    result = get_last_lsrs(n, k)
    print('Case #%d: %d %d' % (case, result[0], result[1]))
