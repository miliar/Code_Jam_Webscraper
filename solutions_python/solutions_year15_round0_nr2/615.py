'''
Created on April 12, 2014

@author: Lior
'''

from math import ceil, floor, sqrt
def eat_perfect(p):
    s = sqrt(p)
    columns = floor(s)
    return columns - 1, ceil(float(p)/columns)

def order_to_columns_lower_than(p, height):
    # returns number of minutes required to bring pile to multiple piles, lower or equal than height
    piles = ceil(float(p)/height)
    return piles-1


def solve(l):
    l.sort(reverse=True)
    special_minutes, eating_time = eat_perfect(l[0])
    max_eating_time = eating_time
    total_special_minutes = special_minutes
    for p in l[1:]:
        if p < max_eating_time:
            break
        total_special_minutes += order_to_columns_lower_than(p, height=eating_time)
    answer = int(max_eating_time + total_special_minutes)
    if answer > l[0]:
        return l[0]
    return answer

def solve2(l):  # will this work?
    max_pile = max(l)
    best_time = max_pile
    for i in xrange(1, max_pile+1):
        time = sum(order_to_columns_lower_than(p, i) for p in l) + i
        if time < best_time:
            best_time = time
    return int(best_time)

def process_files(in_file, out_file):
    num_of_test_cases = int(in_file.next().strip())
    for test_number in xrange(num_of_test_cases):
        print test_number
        D = int(in_file.next().strip())
        plates = [int(p) for p in in_file.next().strip().split(' ')]
        assert len(plates) == D
        result = solve2(plates)
        out_file.write('Case #%d: %s\n' % (test_number+1, result))

if __name__ == '__main__':
    import sys, os
    in_file = sys.argv[1]
    out_file = in_file.replace('.in', '.out')
    with open(in_file, 'rb') as in_file:
        with open(out_file, 'wb') as out_file:
            process_files(in_file, out_file)
