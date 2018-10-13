import sys
def print_result(x, y):
    print 'Case #%d: %.6f' % (x, y)

def float_equal(x, y):
    format = '%.7f'
    return format % x == format % y

def E(n):
    #print 'E', n
    result = 0.0
    i = 1
    while True:
        last = result
        result += i * P(n, i)
        #print 'result : ', result, 'last : ', last
        if float_equal(result, last):
            return result
        i += 1
    return result
p_cache = {}
def P(n, k):
    if (n, k) in p_cache:
        return p_cache[(n, k)]
    if n == 0 and k == 0:
        #print 'P', n, k, 1.0 
        p_cache[(n, k)] = 1.0
        return 1.0
    if n == 0 and k > 0:
        #print 'P', n, k, 0.0
        p_cache[(n, k)] = 0.0
        return 0.0
    if n == 1:
        #print 'P', n, k, 0.0 
        p_cache[(n, k)] = 0.0
        return 0.0
    if n > 1 and k == 0:
        #print 'P', n, k, 0.0
        p_cache[(n, k)] = 0.0
        return 0.0
    result = 0.0
    for i in range(0, n + 1):
        result += P(i, k - 1) * F(n, n - i)

    #print 'P', n, k, result
    p_cache[(n, k)] = result
    return result

def factorial(n):
    if n <= 1:
        return 1
    return reduce(lambda x,y: x*y, xrange(1, n+1))

def F_old(n, m):
    result = factorial(n - m) / 1.0 / factorial(n)
    #print 'F', n, m, result
    return result

f_cache = {}
def F(n, m):
    if (n, m) in f_cache:
        return f_cache[(n, m)]
    l = range(n - m)
    import itertools
    perm = itertools.permutations(l)
    count = 0
    for x in perm:
        flag = False
        for index, item in enumerate(x):
            if index == item:
                flag = True
                break
        if flag == False:
            count += 1
    result = count /1.0 / factorial(m) / factorial(n - m)
    if float_equal(result, 0.0):
        result = 0.0
    f_cache[(n, m)] = result
    return result

def main():
    lines = sys.stdin
    case_num = int(lines.next())
    for i in range(case_num):
        lines.next()
        nums = [int(x) for x in lines.next().strip().split()]
        count = 0
        for index, num in enumerate(nums):
            if not (num == index + 1):
                count += 1
        if count <= 1:
            result = 0.0
        else:
            result = count * 1.0
        #print 'count: ', count
        print_result(i + 1, result)
main()
#for c in range(11, 15):
#    print E(c)
##print F(3, 0)
##print F(3, 1)
##print F(3, 2)
##print F(3, 3)
