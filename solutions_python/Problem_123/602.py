import math
from decimal import *
getcontext().prec = 50

INFINIT = 1000000000L

def adding_steps(current_size, next_size):
    answer = 0
    if current_size == 1:
        return INFINIT, None
#    print current_size, next_size
    while next_size >= current_size:
        current_size += current_size - 1
        answer += 1
    current_size += next_size
    return answer, current_size


def removing_steps(current_size, sizes):
    return len(sizes)

def solve(size0, sizes):
    answer = 0
    current_size = size0
    items_left = len(sizes)
    for size in sizes:
        add, current_size = adding_steps(current_size, size)
        removing_steps = items_left
        items_left -= 1
        if add < removing_steps:
            answer += add
        else:
            answer += removing_steps
            break
    return answer


def should_remove_last(current_size, last_size):
    return current_size <= last_size

def process_case(size0, sizes):
    answer = 0
    sorted_sizes = sorted(sizes)
    answer = solve(size0, sorted_sizes)
    return answer

def read_input():
    s0, n = map(long, raw_input().split())
    array = map(long, raw_input().split())
    return s0, array


def process_input():
    number_of_cases = int(raw_input())
    for case_number in range(1, number_of_cases + 1):
        size0, sizes = read_input()
        answer = process_case(size0, sizes)
        print 'Case #%d: %s' % (case_number, answer)


if __name__ == '__main__':
    process_input()
