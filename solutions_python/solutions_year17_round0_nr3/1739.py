def solution(n, k):
    res_ls = 0
    res_rs = 0
    a = []
    for ii in range(n + 2):
        a.append(0)
    a[0] = 1
    a[-1] = 1

    for ii in range(k):
        jj_list = []
        ls_list = []
        rs_list = []
        min_ls_rs_list = []
        max_ls_rs_list = []
        for jj in range(len(a)):
            if a[jj] == 0:
                for kk in range(jj)[::-1]:
                    if a[kk] == 1:
                        current_ls = jj - kk - 1
                        # print('left: kk', kk, current_ls)
                        break
                for kk in range(jj+1, len(a)):
                    if a[kk] == 1:
                        current_rs = kk - jj - 1
                        # print('right: kk', kk, current_rs)
                        break
                ls_list.append(current_ls)
                rs_list.append(current_rs)
                jj_list.append(jj)
        min_ls_rs_list = [min(ls_list[pp], rs_list[pp]) for pp in range(len(ls_list))]
        min_count = 0
        min_index_list = []

        # print('ls_list:\t', ls_list)
        # print('rs_list:\t', rs_list)

        max_min_ls_rs = max(min_ls_rs_list)
        for jj in range(len(min_ls_rs_list)):
            if min_ls_rs_list[jj] == max_min_ls_rs:
                min_count += 1
                min_index_list.append(jj)
        if min_count == 1:
            selected_index = jj_list[min_index_list[0]]
            selected_index_list = min_index_list[0]
        else:
            max_count = 0
            max_index_list = []
            max_ls_rs_list = [max(ls_list[pp], rs_list[pp]) for pp in min_index_list]
            max_max_ls_rs = max(max_ls_rs_list)
            for jj in range(len(max_ls_rs_list)):
                if max_ls_rs_list[jj] == max_max_ls_rs:
                    max_index_list.append(jj)
                    max_count += 1
            selected_index = jj_list[min_index_list[max_index_list[0]]]
            selected_index_list = min_index_list[max_index_list[0]]

        a[selected_index] = 1
        if ii == k - 1:
            res_ls = ls_list[selected_index_list]
            res_rs = rs_list[selected_index_list]

        # print(a)

    return max(res_ls, res_rs), min(res_ls, res_rs)

if __name__ == '__main__':
    # n = 5
    # k = 2
    # print(solution(n, k))

    num = 0
    src_handle = open('C-small-1-attempt0.in', 'r')
    dst_handle = open('C_small_1_output', 'w')
    test_case_num = 0
    for line in src_handle:
        if num == 0:
            test_case_num = line
            num += 1
            continue
        print('progress:\t', num, test_case_num)
        line = line.strip('\n').split(' ')
        n = int(line[0])
        k = int(line[1])
        max_ls_rs, min_ls_rs = solution(n, k)
        text = 'Case #' + str(num) + ': ' + str(max_ls_rs) + ' ' + str(min_ls_rs) + '\n'
        dst_handle.write(text)
        num += 1
    src_handle.close()
    dst_handle.close()