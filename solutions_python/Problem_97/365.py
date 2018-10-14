from math import factorial


def number_of_combinations(n):
    return factorial(n) / (2 * factorial(n - 2))


def precalculate_recycled_numbers(start, end):
    cache = {}
    for n in xrange(start, end + 1):
        if n in cache:
            continue
        s = str(n)
        recycled_numbers = set()
        recycled_numbers.add(n)
        for i in xrange(len(s)):
            u = s[i:] + s[:i]
            if u[0] == '0':
                continue
            x = int(u)
            if x <= end:
                recycled_numbers.add(x)
        if len(recycled_numbers) > 1:
            for x in recycled_numbers:
                cache[x] = recycled_numbers
    return cache


def get_recycled_numbers(a, b, cache):
    is_calcualted = {}
    result = 0
    for n in xrange(a, b + 1):
        if n in is_calcualted:
            continue
        if n in cache:
            number_of_appropriate_recycled_numbers = 0
            recycled_numbers = cache[n]
            for x in recycled_numbers:
                if x >= a and x <= b:
                    number_of_appropriate_recycled_numbers += 1
                    is_calcualted[x] = True
            if number_of_appropriate_recycled_numbers > 1:
                result += number_of_combinations(number_of_appropriate_recycled_numbers)
    return result

if __name__ == '__main__':
    cache = precalculate_recycled_numbers(1, 2000000)
#    print get_recycled_numbers(100, 500, cache)
#    print get_recycled_numbers(1111, 2222, cache)
#    print get_recycled_numbers(1, 2000000, cache)
    n = input()
    for i in xrange(n):
        a, b = map(int, raw_input().split())
        print 'Case #{}: {}'.format(i + 1, get_recycled_numbers(a, b, cache))
