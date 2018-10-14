#coding=utf-8
#author=godpgf
import fileinput

def get_res(data):
    data_num = list()
    for d in data:
        data_num.append(int(d))
    tidy(data_num)
    res = list()
    is_first = True
    for d in data_num:
        if d == 0 and is_first:
            continue
        is_first = False
        res.append('%d'%d)
    return ''.join(res)


def tidy(data, start_index = 0):
    for i in range(start_index, len(data) - 1):
        if data[i] <= data[i+1]:
            continue
        data[i] -= 1
        for j in range(i+1, len(data)):
            data[j] = 9
        if i > 0 and data[i] < data[i-1]:
            tidy(data, i-1)
        else:
            tidy(data, i+1)


if __name__ == '__main__':
    input = fileinput.input('B-large.in')
    n = int(input.readline())
    for i in range(n):
        data = input.readline()[:-1]
        print "Case #%d: %s" % ((i + 1), get_res(list(data)))