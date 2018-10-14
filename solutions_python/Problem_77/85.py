# -*- coding: utf-8 -*-

INPUT_FILE_PATH = "D-large-975485.in"
OUTPUT_FILE_PATH = "D-large-975485.out"

fr = open(INPUT_FILE_PATH, 'r')
fw = open(OUTPUT_FILE_PATH, 'w')

T = int(fr.readline().strip())

for i in range(T):
    N = int(fr.readline().strip())
    raw_list = fr.readline().strip().split()
    tmp_list = []
    for j in range(N):
        tmp = j + 1
        if tmp != int(raw_list[j]):
            tmp_list.append(int(raw_list[j]))
        else:
            tmp_list.append(-1)

    group_list = []
    index = 0
    for j in range(N):
        if 0 < tmp_list[j]:
            index = j

    while (1):
        hoge_list = []
        while (1):
            tmp = tmp_list[index]
            tmp_list[index] = -1
            if 0 < tmp and not tmp in hoge_list:
                hoge_list.append(tmp)
                index = tmp - 1
            else:
                break
        group_list.append(hoge_list)
        index = -1
        for j in range(N):
            if 0 < tmp_list[j]:
                index = j
                break
        if index < 0:
            break

    # print group_list
    sum = 0.0
    for sl in group_list:
        sum += len(sl)
    print sum
    fw.write("Case #%d: %.6lf\n" % (i + 1, sum))
