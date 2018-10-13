import sys
import os

def __main__():
    case_number = int(input())
    for case in range(case_number):
        line = input()
        max_shyness = int(line.split(' ')[0])
        people = line.split(' ')[-1]
        friends = 0
        sum_people = 0
        for i in range(max_shyness + 1):
            p = int(people[i])
            if p > 0:
                gap = i - sum_people
                if gap > 0:
                    friends += gap
                    sum_people += gap
                sum_people += p
        print('Case #%d: %d' % (case+1, friends))

sys.stdin = open('A-large.in', 'r')
sys.stdout = open('A-large.out', 'w')
__main__()
