__author__ = 'user'
import math
with open('B-large.in') as f:
    with open('b.out', 'w') as out:
        cases = f.readline()
        cases = int(cases)
        for i in xrange(1, cases+1):
            diners_count = int(f.readline())
            diners = map(int, f.readline().split(' '))
            diners = [[diner, 0] for diner in diners]
            max_dine = max((math.ceil(1.0 * diner[0]/(1 + diner[1])) for diner in diners))
            minutes = max_dine
            additional_minutes = 0
            while max_dine > 2:
                for diner in diners:
                    while math.ceil(1.0 * diner[0]/(1 + diner[1])) == max_dine:
                        diner[1] += 1
                        additional_minutes += 1
                max_dine = max((math.ceil(1.0 * diner[0]/(1 + diner[1])) for diner in diners))
                minutes = min(max_dine + additional_minutes, minutes)
            print 'Case #{i}: {res}'.format(res=int(minutes), i=i)
            out.write('Case #{i}: {res}\n'.format(res=int(minutes), i=i))
