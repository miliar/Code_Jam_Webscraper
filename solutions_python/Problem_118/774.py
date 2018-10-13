__author__ = 'deniskrut'

import math
import sys

def checkPalindrome(i):
    s = str(i)
    res = True
    for j in range(0, len(s) / 2):
        if s[j] != s[len(s) - j - 1]:
            res = False
    return res

def palindromesOfLen(desired_len):
    if desired_len == 1:
        return ['0', '1', '2']#, '3', '4', '5', '6', '7', '8', '9']
    if desired_len == 2:
        pal = []
        for s in palindromesOfLen(desired_len - 1):
            pal.append(s + s)
        return pal
    if (desired_len % 2 == 0):
        pal_prev = palindromesOfLen(desired_len - 1)
        pal = []
        for cur_prev_pal in pal_prev:
            left_pal = cur_prev_pal[:(len(cur_prev_pal) / 2)]
            right_pal = cur_prev_pal[(len(cur_prev_pal) / 2 + 1):]
            central_par = cur_prev_pal[len(cur_prev_pal) / 2]
            cur_pal = left_pal + (central_par * 2) + right_pal
            pal.append(cur_pal)
        return pal
    else:
        pal_one = palindromesOfLen(1)
        pal_prev = palindromesOfLen(desired_len - 1)
        pal = []
        for cur_prev_pal in pal_prev:
            left_pal = cur_prev_pal[(len(cur_prev_pal) / 2):]
            right_pal = cur_prev_pal[:(len(cur_prev_pal) / 2)]
            for cur_one_pal in pal_one:
                cur_pal = left_pal + cur_one_pal + right_pal
                pal.append(cur_pal)
        return pal

def palindromesOfLenFiltered(desired_len):
    if desired_len == 1:
        return ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    pal = palindromesOfLen(desired_len)
    res_pal = []
    for cur_pal in pal:
        if cur_pal[0] != '0':
            res_pal.append(cur_pal)
    return res_pal

def palindromeOfSqLen(sq_len):
    pal = palindromesOfLenFiltered(sq_len)
    pal_val = []
    for s in pal:
        i = long(s)
        i_sq = i * i
        if checkPalindrome(i) and checkPalindrome(i_sq):
            pal_val.append(i)
    return pal_val

pal_cache = {}

def palindromeOfSqLenCache(sq_len):
    if sq_len in pal_cache:
        return pal_cache[sq_len]
    else:
        pal_sq_len = palindromeOfSqLen(sq_len)
        pal_cache[sq_len] = pal_sq_len
        return pal_sq_len

def countPalindromeOfSqLen(sq_len):
    return len(palindromeOfSqLen(sq_len))

def countByRange(l, h):
    sl = math.sqrt(l)
    sh = math.sqrt(h)
    count = 0
    for i in range(len(str(long(sl))), len(str(long(sh))) + 1):
        pal_sq_len = palindromeOfSqLenCache(i)
        for cur_pal in pal_sq_len:
            if cur_pal >= sl and cur_pal <= sh:
                count += 1
    return count

t = int(sys.stdin.readline())
res = []
for i in range(0, t):
    lh = sys.stdin.readline().split()
    l = long(lh[0])
    h = long(lh[1])
    count = countByRange(l, h)
    res.append(count)

for i in range(0, t):
    res_str = str(res[i])
    print "Case #" + str(i + 1) + ": " + res_str

#for i in range(1, 50):
    #print i, palindromeOfSqLen(i)

#for i in range(100000, 1000000):
#    if checkPalindrome(i) and checkPalindrome(i * i):
#        print i, i * i