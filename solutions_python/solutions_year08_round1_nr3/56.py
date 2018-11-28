import math
cases = input()

SQRT_FIVE = 2236067977499789696409173668731276235440618359611525724270897245410520925637804899414414408378782274969508176150773783504253267724447073863586360121533452708

PRECISION = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

def pascal_rows(n):
    rows = [[1]]
    for i in xrange(n - 1):
        l_row = rows[-1]
        n_row = [1]
        for i in xrange(len(l_row) - 1):
            n_row.append(l_row[i] + l_row[i + 1])
        n_row.append(1)
        rows.append(n_row)
    return rows

def i_pow(x, y):
    result = 1
    for a in xrange(y):
        result *= x
    return result

for case in xrange(cases):
    v = input()
    pascal = pascal_rows(v+1)
    result = 0
    t_result = 0
    for i, x in enumerate(pascal[-1]):
        if i % 2 == 0:
            result += x * i_pow(3,v-i) * (i_pow(5, i/2))
        else:
            t_result += x * i_pow(3,v-i) * (i_pow(5, i/2))
    result = ((result * PRECISION) + (t_result * SQRT_FIVE))
    result = (result / PRECISION) % 1000
    print 'Case #' + str(case + 1) + ":", '%03d' % int(result)