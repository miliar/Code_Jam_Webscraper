def gcd(num1, num2):
    if num1 > num2:
        for i in range(1,num2+1):
            if num2 % i == 0:
                if num1 % i == 0:
                    result = i
        return result
    elif num2 > num1:
        for i in range(1,num1+1):
            if num1 % i == 0:
                if num2 % i == 0:
                    result = i
        return result
    else:
        result = num1*num2/num1
        return result

def prime_factors(n):
    factors = []
    lastresult = n
    if n == 1:
        return [1]
    while 1:
        if lastresult == 1:
            break
        c = 2
        while 1:
            if lastresult % c == 0:
                break
            c += 1
        factors.append(c)
        lastresult /= c
    return factors

T = input()
for t in xrange(T):
    N = input()
    maxi = 1 if N > 1 else 0
    maxi_bill = 1
    prime_facs = set()
    for n in xrange (2, N+1):
	prime_facs.update(prime_factors(n))
        if maxi_bill % n != 0:
            maxi_bill = maxi_bill * n / gcd(maxi_bill, n)
            maxi += 1
    mini = len(prime_facs)
    print "Case #%d: %d" % (t + 1, maxi - mini)