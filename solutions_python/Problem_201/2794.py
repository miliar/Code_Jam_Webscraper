import collections


def choose(num_stalls, l_s, r_s):
    max_min = 0
    max_min_stalls = collections.defaultdict(list)
    max_max_stalls = collections.defaultdict(list)

    for index in range(num_stalls):
        local_min = min(l_s[index], r_s[index])
        max_min = max(max_min, local_min)
        max_min_stalls[local_min].append(index)

    index = max_min_stalls[max_min][0]
    max_max = max(l_s[index], r_s[index])
    for index in max_min_stalls[max_min]:
        local_max = max(l_s[index], r_s[index])
        max_max = max(max_max, local_max)
        max_max_stalls[local_max].append(index)

    chosen_index = max_max_stalls[max_max][0]
    y = max(l_s[chosen_index], r_s[chosen_index])
    z = min(l_s[chosen_index], r_s[chosen_index])
    for index in range(num_stalls):
        if index < chosen_index:
            r_s[index] = min(r_s[index], chosen_index - index - 1)
        elif index > chosen_index:
            l_s[index] = min(l_s[index], index - chosen_index - 1)
        else:
            l_s[index] = 0
            r_s[index] = 0

    return l_s, r_s, y, z


def main():
    num_cases = int(input())

    for case_num in range(1, num_cases + 1):
        num_stalls, num_entering = [int(num) for num in input().split()]
        min_distance, max_distance = 0, 0
        l_s, r_s = [], []

        for index in range(num_stalls):
            l_s.append(index)
            r_s.append(num_stalls - index - 1)

        for person in range(num_entering):
            l_s, r_s, y, z = choose(num_stalls, l_s, r_s)

        print('Case #{}: {} {}'.format(case_num, y, z))


if __name__ == '__main__':
    main()