#!/usr/bin/python

def solve():
    s_max, people = raw_input().split(' ')
    s_max = int(s_max)
    result = 0
    current_ppl = int(people[0])
    for i in range(1, len(people)):
        if current_ppl < i:
            result += i - current_ppl
            current_ppl += i - current_ppl
        current_ppl += int(people[i])
    return result

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(1, t + 1):
        result = solve()
        print('Case #{0}: {1}'.format(i, result))

