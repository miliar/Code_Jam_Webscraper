def TidyNumbers():
    N = int(input())
    if N < 10:
        return N
    temp = N 

    ten = 10
    result = N

    while temp > 0:
        if isTidy(result): 
            return result

        if (result%ten)/(ten/10) < ( result%(ten * 10 ))/ten:
            result = (result / ten)*ten - 1
        ten *= 10
        temp /= 10


    return int(0)

def isTidy(num):
    digit = num%10
    num = num/10
    while num > 0: 
        if digit < num%10:
            return False
        else:
            digit = num % 10 
            num /= 10 
    return True

for case in xrange(input()):
    print 'Case #%d: %d' % (case+1, TidyNumbers())
