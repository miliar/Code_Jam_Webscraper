def get_final_ls_rs(n, k):
    e_list = [n]
    for j in range(1, k):
        num = max(e_list)
        max_index = e_list.index(num)
        left_list = e_list[0: max_index + 1]
        right_list = e_list[max_index + 1: len(e_list)]

        if num % 2 == 0:
            left_list[len(left_list) - 1] = num/2 - 1
            left_list.append(num/2)
        else:
            left_list[len(left_list) - 1] = num/2
            left_list.append(num/2)

        e_list = left_list + right_list

    max_empty = max(e_list)

    ls = max_empty / 2 -1 if max_empty % 2 == 0 else max_empty / 2
    rs = max_empty / 2

    return max(ls, rs), min(ls, rs)


t = int(raw_input())
for i in xrange(1, t + 1):
    numbers = raw_input().split(" ")
    outputs = get_final_ls_rs(int(numbers[0]), int(numbers[1]))
    print "Case #%d: %d %d" % (i, outputs[0], outputs[1])
