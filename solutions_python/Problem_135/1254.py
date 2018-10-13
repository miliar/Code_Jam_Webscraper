import sys

large = "A-large-practice.in"
small = "A-small-attempt1.in"
example = "example"
use_small = 1
stdin = 0

def main(argv):
    f = get_file(argv)

    cases = int(f.readline())
    for i in range(cases):
        ri = int(f.readline()) -1
        mat = [map(int, f.readline().split(" ")) for x in xrange(4)]
        row = mat[ri]
        ri2 = int(f.readline()) -1
        mat2 = [map(int, f.readline().split(" ")) for x in xrange(4)]
        row2 = mat2[ri2]
        ins = set(row).intersection(row2)
        if(len(ins) == 0):
            res = "Volunteer cheated!"
        elif(len(ins) == 1):
            res = ins.pop()
        else:
            res = "Bad magician!"

        print "Case #{}: {}".format(i +1, res)

    f.close()


def solution(row, mat):

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