import sys
import bisect

large = "D-large.in"
small = "D-small-attempt0.in"
example = "example"
use_small = 0
stdin = 0

def main(argv):
    f = get_file(argv)

    b = bisect.bisect_right([1.0, 5.0, 6.0], 8.1)

    cases = int(f.readline())
    for case in range(cases):
        n = int(f.readline())
        naomi = map(float, f.readline().split(" "))
        ken   = map(float, f.readline().split(" "))

        res1, res2 = solution(n, naomi, ken)

        print "Case #{}: {} {}".format(case +1, res1, res2)


    f.close()


def solution(n, naomii, kenn):

    naomi = sorted(naomii)
    ken = sorted(kenn)
    l = 0
    g = []
    for i in xrange(n):

        nao = naomi.pop(0)
        ke = bisect.bisect_right(ken,nao)
        if(ke >= len(ken)):
            l+=1
            ken.pop(0)
        else:
            del ken[ke]
        # if ken[i] < naomi[i]:
        #     l+=1

    naomi = sorted(naomii)
    ken = sorted(kenn)
    # ken.reverse()
    a=0
    for i in xrange(n):
        if naomi[-1] > ken[-1]:
            naomi.pop()
            ken.pop()
            a+=1
        else:
            naomi.pop(0)
            ken.pop()

        # if ken[i] < naomi[i]:
        #     a+=1


    return a, l

def get_file(argv):
    if stdin:
        return sys.stdin
    # if len(argv) == 2:
    #     f = open(argv[1], 'r')
    # else:
    # f = open(example)
    f = open(small if use_small else large)
    return f



if __name__ == "__main__":
    main(sys.argv)