import pp
import sys

def calc(n, cars):
    is_available = [True] * n
    def is_valid(s):
        a = [False] * 26
        i = 0
        while i < len(s):
            index = ord(s[i]) - 97
            if a[index]:
                return False
            a[index] = True
            i += 1
            while i < len(s) and s[i] == s[i - 1]: i += 1

        return True

    def calc_mask(s):
        mask = 0
        for ch in s:
            index = ord(ch) - 97
            mask |= (1 << index)

        return mask


    cars = [car for car in cars if is_valid(car)]
    if n != len(cars):
        return 0
    n = len(cars)
    masks = [calc_mask(car) for car in cars]

    def can_move(last, i, mask):
        if last == '':
            return True

        if last == cars[i][0]:
            index = ord(last) - 97
            mask = mask & (~(1 << index))

        return (mask & masks[i]) == 0

    def calc(k, last, curr_mask):
        if k == 0:
            return 1
        result = 0

        for i in xrange(n):
            if is_available[i] and can_move(last, i, curr_mask):
                is_available[i] = False
                result += calc(k - 1, cars[i][-1], curr_mask | masks[i])
                is_available[i] = True

        return result

    return calc(n, '', 0)

job_server = pp.Server()

f = open('B-small-attempt2.in', 'r')
T = int(f.readline()) + 1

jobs = []
for test in xrange(1, T):
    n = int(f.readline())
    cars = f.readline().split()
    jobs.append(job_server.submit(calc,(n,cars)))

f.close()

open('output.txt', 'w').write('\n'.join(['Case #%d: %s' % (i + 1, str(job())) for i, job in enumerate(jobs)]))
