from heapq import heappush, heappop

value_list = []

def middle_lvalue(v):
    if v % 2 == 0:
        return v / 2 - 1
    return v / 2


def middle_rvalue(v):
    if v % 2 == 0:
        return v / 2
    return v / 2


def get_result(v):
    v = v * (-1)
    if v % 2 == 0:
        ls = v / 2 - 1
        rs = v/2
    else:
        ls = rs = v / 2
    return ls, rs


if __name__ == '__main__':
    
    t = int(raw_input())  # read a line with a single integer
    for case in xrange(1, t + 1):
        #print "Case #", case
        line = raw_input()
        n = int(line.split(' ')[0])
        k = int(line.split(' ')[1])
        #print "n, k", n, k
        value_list = []
        heappush(value_list, -n)
        for i in range(0, k-1):
            #print value_list
            biggest = heappop(value_list) * (-1)
            #print biggest
            ls = middle_lvalue(biggest)
            rs = middle_rvalue(biggest)
            heappush(value_list, -ls)
            heappush(value_list, -rs)
        #print_list(node)
        v = heappop(value_list)
        ls, rs = get_result(v)
        print "Case #{}: {} {}".format(case, rs, ls)