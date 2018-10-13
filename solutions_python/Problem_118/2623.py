# -*- coding:utf-8 *-*

import numpy
import csv

def fair(num):
    fc = str(num)
    for i in range(len(fc) // 2):
        if fc[i] != fc[len(fc) -1 -i]:
            return False
    else:
        return True

def square(start, end):
    ans = []
    for i in range(start, end + 1):
        if int(i ** 0.5) == i ** 0.5:
            ans.append(int(i ** 0.5))
            break
    for j in range(end, start - 1, -1):
        if int(j ** 0.5) == j ** 0.5:
            ans.append(int(j ** 0.5))
            break
    if ans:
        return range(ans[0], ans[1] + 1)
    else:
        return []

def fs(data_set):
    ans = []
    for data in data_set:
        sq = square(data[0], data[1])
        #print(sq)
        sqf = []
        for s in sq:
            if fair(s):
                sqf.append(s)
        sqfa = numpy.array(sqf)
        #print(sqfa)
        sqfa2 = sqfa * sqfa
        an = 0
        for s2 in sqfa2:
            if fair(s2):
                an += 1
        ans.append(an)
    return ans


if __name__ == '__main__':
    f = 'C-small-attempt2.in'
    data_set = []
    for (inx, data) in enumerate(csv.reader(open(f), delimiter= ' ')):
        if inx == 0:
            continue
        data_set.append([int(d) for d in data])
    print(data_set)
    with open('fs_ans', 'w') as f:
        for (inx, data) in enumerate(fs(data_set)):
            f.write('Case #{0}: {1}\n'.format(inx + 1, data))



