import numpy as np


def diff(n,i):
    return int(n[i+1])-int(n[i])


def tidy_up(num):
    n = []
    for i in str(num):
        n.append(i)
    for i in range(len(n)-1):
        if diff(n,i) < 0:
            for j in range(i, len(n)-1):
                n[j+1] = '0'

    num = int(''.join(n))
    return num


def tidy_test(num):
    n = []
    for i in str(num):
        n.append(i)

    tidy = True
    if len(n) > 1:
        for i in range(len(n)-1):
            if diff(n,i) < 0:
                tidy = False
    return tidy


f_o = open('O_b_large.txt', 'w')
with open('b_large.txt', 'r') as f:
    dat = f.readlines()

dat = [n.split('\n')[0] for n in dat[1:]]

# print dat[:10]

for i, num in enumerate(dat):
    while not tidy_test(num):
        num = tidy_up(num) - 1
    print num
    f_o.writelines("Case #{}: {}\n".format(i+1, num))

f_o.close()
