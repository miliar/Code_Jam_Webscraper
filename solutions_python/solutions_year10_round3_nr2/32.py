import math

def get_num_tests(L, P, C):
    num = math.log(math.log(float(P)/L, C), 2)
    num, r = divmod(num, 1.0)
    if r > 0.0:
        num += 1
    if num <0: num = 0
    return num

def run(f):
    case_num = int(f.readline())
    for i in xrange(case_num):
        L, P, C = map(int, f.readline().split())
        print "Case #%d: %d" % (i+1, get_num_tests(L, P, C))
            
if __name__ == '__main__':
    import sys
    run(open(sys.argv[1]))