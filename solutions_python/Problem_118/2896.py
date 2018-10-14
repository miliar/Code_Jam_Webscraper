__author__ = 'nilsonjr'

import math

def isapalindrome(num):
    s_num = str(num)
    size = len(s_num)
    for i in range(int(math.floor(len(s_num)/2))):
        if s_num[i] != s_num[size - i - 1]:
            return False
    return True

def havesqrt(num):
    r = math.sqrt(int(num))
    return r % 1 == 0, r

def fands(num):
    if isapalindrome(num):
        have, r = havesqrt(num)
        if have and isapalindrome(int(r)):
            return True
    return False


f = open('/Users/nilsonjr/PycharmProjects/gj/C-small-attempt0.in')
f_res = open('res.txt', 'w')
n_lines = int(f.readline())

for idx in range(n_lines):
    line = f.readline()
    l_aux = line.split()
    i1 = int(l_aux[0])
    i2 = int(l_aux[1])+1

    count = 0
    for i in range(i1, i2):
        if fands(i):
            count += 1
    f_res.write("Case #"+str(idx+1)+": "+str(count)+"\n")
