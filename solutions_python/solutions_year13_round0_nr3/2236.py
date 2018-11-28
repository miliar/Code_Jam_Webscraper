import math


def check_good_squre(n):
    b = math.sqrt(n)
    return b == int(b)

def check_number_fair(n):
    if n < 10:
        return True
    l = list(str(n))
    length = len(l) - 1

    for i in xrange(length):
#        print "i:%d j:%d" % (i, length - i)
        if l[i] != l[length - i]:
            return False
    return True
        
def check_fair_and_square(begin, end):
    count=0
    for n in range(begin, end+1):
        if not check_good_squre(n):
            continue
        sqrtnum = int(math.sqrt(n));
        if not check_number_fair(n):
            continue
        if not check_number_fair(sqrtnum):
            continue
        count += 1
    return count


# Pass the deal function.
def googleJamReadCase(filename, func):
    with open(filename) as f:
        casenum = int(f.readline())
        for casei in range(casenum):
            a,b = map(int,list(f.readline().strip('\n').split(' ')));

            result = func(a,b)
            print "Case #%d: %d" % (casei + 1, result)

if __name__ == '__main__':
    import sys
    googleJamReadCase(sys.argv[1], check_fair_and_square)
