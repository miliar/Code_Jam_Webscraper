import sys
import math

large = "A-large-practice.in"
small = "small.in"
example = "example.txt"
stdin = 0

def main(argv):
    f = get_file(argv)

    cases = int(f.readline())
    for i in range(cases):
        elf, all =map(float,f.readline().split("/"))
        res = 0
        lf = math.log(all,2)
        li = int(lf)
        if(lf > 40) or (lf - li > 0.0):
            res = "impossible"
        else:
            dec = elf / all
            par_sum = dec * 2
            j=0
            while 1:
                if(j > 40):
                    res = "impossible"
                    break
                big_anc = 1.0/ (2.0**j)
                if par_sum - big_anc >= 0:
                    res = j + 1
                    break
                j+=1

        print "Case #{}: {}".format(i +1,  res)

    f.close()


def solution(row, mat):

    return 1

def get_file(argv):
    # if stdin:
    #     return sys.stdin
    # if len(argv) == 2:
    #     f = open(argv[1], 'r')
    # else:
    f = open(small)
    # f = open(small)
    # f = open(large)
    return f



if __name__ == "__main__":
    main(sys.argv)