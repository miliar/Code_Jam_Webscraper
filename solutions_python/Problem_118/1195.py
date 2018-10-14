import math

def int_to_list(a):
    l = []
    while a >= 10:
        l.append(a % 10)
        a /= 10
    else:
        l.append(a)
    return l

def is_reverse(x):
    x = int_to_list(x)
    y = list(x)
    y.reverse()
    if x == y: 
        return True
    else:
        return False

def main():
    test_cnt = int(raw_input())
    for times in xrange(test_cnt):
        cnt = 0
        a ,b = [int(x) for x in raw_input().split()]
        a = int(math.ceil(math.sqrt(a)))
        b = int(math.floor(math.sqrt(b)))
        for x in xrange(a, b+1):
            if is_reverse(x) and is_reverse(x * x):
                cnt += 1
        else:
            print 'Case #%d: %d' % (times + 1, cnt)

if __name__ == '__main__':
    main()
