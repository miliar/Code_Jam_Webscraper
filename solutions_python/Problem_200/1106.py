#!/usr/bin/python
#-*- coding: utf8 -*-

''' Template for Google Code Jam '''

import sys

def main():
    ''' main '''
    case_num = int(sys.stdin.readline())
    for i in range(1, case_num+1):
        line = sys.stdin.readline().rstrip()
        args = line.split(' ')
        #answer = solve_small(int(args[0]))
        answer = solve_large(int(args[0]))
        print('Case #{0:d}: {1}'.format(i, answer))
        #print('Case #{0:d}: {1}'.format(i, args[0] + ' ' + str(answer)))

def solve_small(num):
    ''' solve problem '''
    if num < len(memo):
        for i in range(num, 0, -1):
            if isTidy(i):
                return i
    else:
        return False

def isTidy(num):
    key_num = 9
    while num != 0:
        mod_num = num % 10
        num = int(num / 10)
        if key_num < mod_num:
            return False
        else:
            key_num = mod_num
    return True

def solve_large(num):
    #321876 -> 321799 -> 299999
    numbers = [int(i) for i in list(str(num))]

    tmp_key = 0
    for i in range(0, len(numbers)):
        # if tidy
        if numbers[i] >= tmp_key:
            tmp_key = numbers[i]
        # if not tidy, make tidy
        else:
            for j in range(i, 0, -1):
                numbers[j] = 9
                numbers[j-1] -= 1
                if j-1 == 0 or numbers[j-1] >= numbers[j-2]:
                    break
            for j in range(i+1, len(numbers)):
                numbers[j] = 9
            break

    return int(''.join(map(str, numbers)))

# tidy memo
memosize = 10000
memo = [False] * (memosize + 1)
for i in range (0, len(memo)):
    if isTidy(i):
        memo[i] = True

if __name__ == '__main__':
    #print(solve_large(110))
    main()
    # print(isTidy(1000))
    # print(isTidy(999))
    # print(isTidy(989))
