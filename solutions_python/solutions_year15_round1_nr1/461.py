
def read_array(convertor=None):
    ret = raw_input().split()
    if convertor: ret = map(convertor, ret)
    return ret


def cal1(m):
    return sum(filter(lambda x:x>=0, map(lambda x: x[0]-x[1], zip(m[:-1], m[1:]))))

def cal2(m):
    MAX = -777777777
    min_speed = max([MAX] + filter(lambda x:x>=0, map(lambda x: x[0]-x[1], zip(m[:-1], m[1:]))))

    if min_speed == MAX:
        return 0
    return sum(map(lambda x:min(x, min_speed), m)[:-1])


def main():
    for t in range(1, 1+input()):
        N = input()
        m = read_array(int)
        print "Case #%d: %d %d" % (t, cal1(m), cal2(m))
    pass



main()
