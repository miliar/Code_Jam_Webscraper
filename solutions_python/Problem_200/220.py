def solve(n):
    decimal = str(n)
    if ''.join(sorted(decimal)) == decimal: return n

    ret = int('9' * (len(decimal)-1))
    for i in range(len(decimal)):
        if i and decimal[i-1] > decimal[i]: break

        lo = 1 if i == 0 else int(decimal[i-1])
        hi = int(decimal[i])

        for digit in range(lo, hi):
            cand = decimal[:i] + str(digit) + ('9' * (len(decimal) - i - 1))
            ret = max(ret, int(cand))
    return ret

cases = int(input())
for c in range(cases): 
    print('Case #%d: %d' % (c+1, solve(int(input()))))

