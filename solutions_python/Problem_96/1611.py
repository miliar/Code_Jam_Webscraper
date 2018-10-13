vals = [[0, 0], [1, 1], [1, 2], [1, 2], [2, 2], [2, 3],
        [2, 3], [3, 3], [3, 4], [3, 4], [4, 4], [4, 5],
        [4, 5], [5, 5], [5, 6], [5, 6], [6, 6], [6, 7],
        [6, 7], [7, 7], [7, 8], [7, 8], [8, 8], [8, 9],
        [8, 9], [9, 9], [9, 10], [9, 10], [10, 10], [10, 10], [10, 10]]

with open('B-large.in', 'r') as f:
    with open('outB-large.in', 'w') as f1:
        f.readline()
        cnt = 1
        for line in f:
            line = [int(x) for x in line.split()]
            n = line[0]
            s = line[1]
            p = line[2]
            ti = line[3:]
            ti.sort()

##            if s:
##                s = 1
##            else:
##                s = 0

            ans = 0

            for t in ti:
                if s:
                #print t, vals[t][s], p
                    if vals[t][1] >= p:
                        ans += 1
                        s -= 1
                else:
                    if vals[t][0] >= p:
                        ans += 1

            f1.write('Case #{}: {}\n'.format(cnt, ans))
            cnt += 1
