LOW_LIMIT = 0

def is_tidy(num):
    tidy = True
    previous = num[0]
    for i in num[1:]:
        if previous > i:
            tidy = False
            break
        previous = i
    return tidy

def tidy(num):

    if is_tidy(num)==1:
        return num

    previous = num[0]
    size     = 1
    pivot    = 0
    for index,i in enumerate(num[1:]):
        if previous < i:
            pivot = index+1
            previous = i
            size = 1
        elif previous == i:
            previous = i
            size += 1
        else:
            break

    list_num   = list(num)
    list_num[pivot] = str( int(num[pivot]) - 1 )
    for i in xrange(pivot+1, len(num)):
        list_num[i] = '9'

    return ''.join(list_num).lstrip('0')


def solve():
    t = int (raw_input())
    for i in xrange(1, t + 1):
        n = raw_input()
        print "Case #{}: {}".format(i, tidy(n))

solve()
