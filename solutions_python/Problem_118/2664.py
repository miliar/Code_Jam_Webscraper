#!/usr/bin/python3
"""
python Cpalidromes.py < IN-FILE.in > OUT-FILE.out
python Cpalidromes.py < IN-FILE.in | tee OUT-FILE.out
"""
from cmath import sqrt


def _get_fair_and_square(begin, end):
    for num in range(begin, end + 1):
        str_num = str(num)
        if str_num.endswith('0'):
            continue
        if str_num == str_num[::-1]:
            sqr_num = sqrt(num)
            if sqr_num.real.is_integer():
                str_sqr_num = str(int(sqr_num.real))
                # no need to check endswith('0')
                if str_sqr_num == str_sqr_num[::-1]:
                    yield num


cache = []  # more read optimized bTree?

# prepopulate with fair-and-square < 1000
cache = list(_get_fair_and_square(1,1000))
cache_begin, cache_end = 1, 1000



def get_fair_and_square_count(begin, end):
    global cache_end
    if begin > cache_end or end > cache_end:
        next_cached_end = max(end, cache_end+1000)
        for num in _get_fair_and_square(cache_end+1, next_cached_end):
            cache.append(num)
        cache_end = next_cached_end
    t = 0
    for n in cache:
        if n < begin:
            continue
        if n > end:
            break
        t += 1
    return t



def solve(num_cases):
    for i in range(1, num_cases+1):
        case = input().split(' ')
        range_begin, range_end = int(case[0]), int(case[1])
        solved = get_fair_and_square_count(range_begin, range_end)
        print('Case #{num}: {solved}'.format(num=i, solved=solved))

if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
