from sys import stdin


MAX = 10**50
SMALL_MAX = 35

def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]

def fair_and_nice(n):
    results = []
    for i in range(n):
        if is_palindrome(i):
            ii = i*i
            if is_palindrome(ii):
                results.append(ii)
    return results

def query_count(L, a, b):
    count = 0
    for item in L:
        if item >= a and item <= b:
            count += 1
    return count


table = fair_and_nice(SMALL_MAX)

T = raw_input()
for case, line in enumerate(stdin):
    A, B = map(long, line.split())

    ans = query_count(table, A, B)
    print 'Case #{0}: {1}'.format(case+1, ans)
