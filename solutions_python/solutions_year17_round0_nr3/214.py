#coding=utf-8
#author=godpgf
import fileinput
import math

def get_l_r(n):
    ln = 0
    rn = 0
    if n % 2 == 0:
        ln = n / 2
        rn = ln - 1
    else:
        ln = n / 2
        rn = ln
    return ln, rn


def get_res(n, k):
    if n == k:
        return 0, 0
    #n个位置，选了一个，剩下左右各几个,设左边大于等于右边
    ln, rn = get_l_r(n)
    if k == 1:
        return ln, rn
    #k个人，选了一个放中间，剩下的左右左右的顺序依次去两边
    lk, rk = get_l_r(k)
    if lk > rk:
        #最后那个人一定去了左边
        return get_res(ln, lk)
    else:
        return get_res(rn, rk)



if __name__ == '__main__':
    input = fileinput.input('C-large.in')
    n = int(input.readline())
    for i in range(n):
        data = input.readline()[:-1]
        l, r = get_res(int(data.split(' ')[0]), int(data.split(' ')[1]))
        print "Case #%d: %d %d" % ((i + 1), l, r)