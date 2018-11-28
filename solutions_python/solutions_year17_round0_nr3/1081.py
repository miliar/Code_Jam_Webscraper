#!/usr/bin/python
#-*- coding: utf8 -*-

''' Template for Google Code Jam '''

import sys
import heapq

def main():
    ''' main '''
    case_num = int(sys.stdin.readline())
    for i in range(1, case_num+1):
        line = sys.stdin.readline().rstrip()
        args = line.split(' ')
        answer = solve(int(args[0]), int(args[1]))
        print('Case #{0:d}: {1}'.format(i, answer))

def solve(room_num, person_num):
    ''' solve problem '''
    bathrooms = [(-room_num, room_num)]
    heapq.heapify(bathrooms)
    memo = (0, 0)
    for i in range(0, person_num):
        # pop
        tmp = heapq.heappop(bathrooms)
        # push
        # 4 -> 2, 1, 5->2, 2
        key = int(tmp[1] * 0.5)
        if tmp[1] % 2 == 0:
            heapq.heappush(bathrooms, (-key, key))
            heapq.heappush(bathrooms, (-(key-1), (key-1)))
            memo = (key, key-1)
        else:
            heapq.heappush(bathrooms, (-key, key))
            heapq.heappush(bathrooms, (-key, key))
            memo = (key, key)

    return ' '.join(map(str, memo))

if __name__ == '__main__':
    main()
