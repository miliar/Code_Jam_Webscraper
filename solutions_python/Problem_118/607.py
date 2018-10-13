import sys
from math import sqrt, floor, ceil

def palindrome(n):
    s = str(n)
    for i in xrange(len(s)):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

def numbers(size):
    num = 1
    for _ in xrange(size-1):
        num *= 10;
    upper_bound = num*10
    while num < upper_bound:
        yield num
        num += 1

def gen_palindromes(size):
    #print "gen_palindromes(size):", size
    left_part_size = int(ceil(size/2.0))
    #print "left_part_size:", left_part_size
    for num in numbers(left_part_size):
        #print "num:", num
        yield int( str(num) + "".join([i for i in reversed(str(num)[:size-left_part_size])]) )

def gen_fair_sqrt_palindromes(start, end):
    #print "gen_fair_sqrt_palindromes(start, end):", start, end
    #for curr_num in xrange(start, end+1):
    size = 1
    while True:
        for curr_num in gen_palindromes(size):
            if curr_num >= start:
                if curr_num > end:
                    return
                #print "curr_num:", curr_num
                if palindrome(curr_num * curr_num):
                    yield curr_num * curr_num
        size += 1


T = int(sys.stdin.readline())
fair_palindromes = list(gen_fair_sqrt_palindromes(1, pow(10, 7)))
for case in xrange(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    
    x = 0
    for i in fair_palindromes:
        if i >= A and i <= B:
            x += 1
    
    print "Case #"+str(case)+": "+str(x)
