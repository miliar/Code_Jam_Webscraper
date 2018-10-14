__author__ = 'linfuyuan'
# -*- coding: utf-8 -*-

with open('output.txt', 'w') as of:
    with open('A-large.in') as f:
        caseNum = int(f.readline().strip())
        for i in range(caseNum):
            data = f.readline().strip().split(' ')
            smax = int(data[0])
            fri_num, stand_num = 0, 0
            for j in range(smax + 1):
                if stand_num >= j:
                    stand_num += int(data[1][j])
                else:
                    fri_num += j - stand_num
                    stand_num += j - stand_num + int(data[1][j])
            of.write("Case #%d: %d\n" % (i + 1, fri_num))
