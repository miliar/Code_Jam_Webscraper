import sys

large = "B-large.in"
small = "B-small-attempt0.in"
example = "example"
use_small = 0
stdin = 0

def main(argv):
    f = get_file(argv)

    cases = int(f.readline())
    for i in range(cases):
        C, F, X = map(float, f.readline().split(" "))
        res = solution(C, F, X)
        print "Case #{}: {:.7f}".format(i +1, res)

    f.close()


def solution(c, f, x):

    i = 0
    spend = 0
    speed = 2
    while True:

        current = (x / speed) + spend
        spend += c / speed
        speed += f
        future = (x / (speed)) + spend
        if(current < future):
            return current
        # spend +=
        # i+=1

    return 1

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