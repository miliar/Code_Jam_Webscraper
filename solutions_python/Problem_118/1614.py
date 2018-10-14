#!/usr/bin/env python

import math
import bisect

def create_palin():
    palin = set() 
    for i in range(1001):
        n = i if i != 0 else '' 
        new_str = str(n) + str(n)[::-1]
        if new_str != '':
            palin.add(int(new_str)) 
        m = len(new_str) / 2
        for j in range(10):
            new_str1 = new_str[:m] + str(j) + new_str[m:]
            palin.add(int(new_str1))
    return sorted(list(palin))

def is_palin(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
        return True
    return False

def get_num_palindromes(A, B, palindrome_list):
    fair_and_square_palins = 0
    a = math.sqrt(A)
    b = math.sqrt(B) + 1
    index = bisect.bisect_left(palindrome_list, a)
    for i in range(index, len(palindrome_list)):
        p = palindrome_list[i]
        if p * p > B:
            break
        if is_palin(p) and is_palin(p * p) and p * p >= A:
            fair_and_square_palins += 1
    return fair_and_square_palins

if __name__ == '__main__':
    palindrome_list = create_palin()

    tc = int(raw_input())
    for t in range(tc):
        A, B = map(int, raw_input().split())
        print 'Case #%d: %d' % (t + 1, get_num_palindromes(A, B, palindrome_list)) 
