from decimal import *

def process_problem(price, increase, target, rate):
    answer = 0
    while (1):
        candidate1 = target / rate
        candidate2 = (price / rate) + (target / (rate + increase))
        if candidate1 < candidate2:
            return answer + candidate1
        else:
            answer += (price / rate)
            rate += increase

with open('B-large.in', 'rb') as f:
    num_problems = int(f.next())
    i = 0
    for line in f:
        problem = [Decimal(x) for x in line.split(' ')]
        print 'Case #%d: %.7f' % (i + 1, process_problem(problem[0], problem[1], problem[2], 2))
        i += 1

            
        
