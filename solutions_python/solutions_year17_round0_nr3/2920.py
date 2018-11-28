# -*- coding: utf-8 -*-
__author__ = "Sommily"

input = """5
4 2
5 2
6 2
1000 1000
1000 1"""

input = """100
4 2
5 2
6 2
1000 1000
1000 1
1000 512
914 728
500 499
5 1
1000 489
1000 128
1000 500
1000 499
500 116
1000 2
307 300
316 283
4 1
696 618
500 248
1000 488
999 511
1000 503
1000 498
999 487
361 326
969 933
746 698
2 2
500 117
500 2
905 878
500 128
796 610
799 639
500 250
500 1
664 588
1000 999
999 512
751 668
370 335
452 364
760 701
344 279
999 497
380 340
636 546
999 255
3 2
500 127
648 592
500 91
500 245
295 284
500 500
999 2
652 608
864 663
999 498
999 256
500 255
823 656
560 472
404 377
260 209
565 533
543 449
999 1
431 334
500 251
999 499
500 156
965 760
999 127
280 256
999 261
797 676
999 488
1 1
1000 282
1000 255
999 999
259 218
2 1
3 1
500 249
323 255
999 998
999 128
1000 511
726 646
500 244
942 902
969 921
895 887
1000 256
1000 127
268 244
500 256"""


def find_max_empty_stall_list(all_stall):
    # print filter(lambda x: x[1] == 1, all_stall)
    start_i = max_stall_start_i = None
    max_interval = stall_interval = 0

    for stall in all_stall:
        if start_i is None and stall[1] == 1:
            continue

        if stall[1] == 0 and start_i is None:
            start_i = stall[0]
            stall_interval = 0
            continue

        stall_interval += 1
        if stall[1] == 1:
            if max_interval < stall_interval:
                max_interval = stall_interval
                max_stall_start_i = start_i
            stall_interval = 0
            start_i = None


    return max_stall_start_i, max_interval


def find_user_stall(max_stall_start_i, max_interval):
    right_stall = (max_stall_start_i + max_interval / 2, 1)
    return right_stall


def init_all_stall(N):
    all_stall = [(0, 1)]
    for i in range(1, N + 1, 1):
        all_stall.append((i, 0))
    all_stall.append((i + 1, 1))
    return all_stall


def user_in_stall(all_stall, user_stall):
    new_stall_list = []
    for stall in all_stall:
        if stall[0] != user_stall[0]:
            new_stall_list.append(stall)
        else:
            new_stall_list.append(user_stall)
    return new_stall_list


def get_right_left_range(start_i, end_i, stall_i):
    return stall_i - start_i, end_i - stall_i - 1


def calc(N, K):
    all_stall = init_all_stall(int(N))
    for person_num in range(1, int(K) + 1):
        max_stall_start_i, max_interval = find_max_empty_stall_list(all_stall)
        user_stall = find_user_stall(max_stall_start_i, max_interval)
        new_all_stall = user_in_stall(all_stall, user_stall)
        assert new_all_stall != all_stall
        all_stall = new_all_stall

    right_range, left_range = get_right_left_range(max_stall_start_i, max_stall_start_i + max_interval, user_stall[0])
    return max(right_range, left_range), min(right_range, left_range)


if __name__ == "__main__":
    # print calc("100", "21")

    # all_stall = init_all_stall(4)
    # print(all_stall)
    # max_stall_start_i, max_interval = find_max_empty_stall_list(all_stall)
    # print(max_stall_start_i, max_interval)
    # print(find_user_stall(max_stall_start_i, max_interval))
    #
    # all_stall = [(0, 1), (1, 0), (2, 1), (3, 0), (4, 0), (5, 1)]
    # print(all_stall)
    # max_stall_start_i, max_interval = find_max_empty_stall_list(all_stall)
    # print(max_stall_start_i, max_interval)
    # print(find_user_stall(max_stall_start_i, max_interval))

    #
    # all_stall = [(0, 1), (1, 0), (2, 0), (3, 1), (4, 0), (5, 0), (6, 1)]
    # print(all_stall)
    # max_stall_start_i, max_interval = find_max_empty_stall_list(all_stall)
    # print(find_right_stall(max_stall_start_i, max_interval))
    #

    lines = input.split("\n")
    count = int(lines[0])

    for i in range(1, count + 1):
        N = lines[i].split(' ')[0]
        K = lines[i].split(' ')[1]

        if N == K:
            print("Case #{}: 0 0".format(i))

        else:
            max_range, min_range = calc(N, K)
            print("Case #{}: {} {}".format(i, max_range, min_range))
