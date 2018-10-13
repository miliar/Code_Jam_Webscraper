import bisect


def main():
    T = int(input())
    N = list()
    K = list()
    for i in range(T):
        n, k = map(int, input().split())
        N.append(n)
        K.append(k)

    for i in range(T):
        stall_list = [0, N[i] + 1]
        stall_list.insert(1, (1 + N[i]) // 2)
        Ls = stall_list[1] - stall_list[0] - 1
        Rs = stall_list[len(stall_list) - 1] - stall_list[1] - 1
        # import pdb; pdb.set_trace()
        k = K[i] - 1
        if N[i] == K[i]:
            Ls = 0
            Rs = 0
            k = 0

        while k != 0:
            gap_list = []
            gap = 0
            for w in range(1, len(stall_list)):
                gap = stall_list[w] - stall_list[w - 1] - 1
                gap_list.append(gap)

            gap_index = gap_list.index(max(gap_list))
            selected_stall = (stall_list[gap_index + 1] + stall_list[gap_index]) // 2
            bisect.insort(stall_list, selected_stall)
            Ls = stall_list[stall_list.index(selected_stall)] - stall_list[stall_list.index(selected_stall) - 1] - 1
            Rs = stall_list[stall_list.index(selected_stall) + 1] - stall_list[stall_list.index(selected_stall)] - 1
            k = k - 1

        print("Case #{}: {} {}".format(i + 1, max(Ls, Rs), min(Ls, Rs)))


if __name__ == '__main__':
    main()
