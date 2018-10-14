from math import factorial
T = int(raw_input())

memo = {}
def solve(first, last, lastpos):
    key = (first, last, lastpos)
    if key in memo:
        return memo[key]
    else:
        if first == lastpos:
            # return possible subsequence
            length = lastpos - 2
            n =  (last - 1) - (first + 1) + 1
            if n >= length:
                res = factorial(n) / ( factorial(length) * factorial(n - length) )
            else:
                res = 0
        else:
            res = 0
            n = (last - 1) - (lastpos + 1) + 1
            offs = last - lastpos
            for pos in range(max(lastpos - offs, 2), lastpos):
                # subsequence here too
                k = lastpos - (pos + 1)
                c = factorial(n) / ( factorial(k) * factorial(n - k))
                res += solve(first, lastpos, pos) * c
        memo[key] = res
        return res

for t in range(T):
    n = int(raw_input())

    solutions = 1
    for i in range(2, n):
        maxpos = n-i+1
        for j in range(i, maxpos+1):
            solutions += solve(i, n, j)

    print "Case #%d: %d" % (t+1, solutions % 100003)

