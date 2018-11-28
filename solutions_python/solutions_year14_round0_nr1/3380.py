import sys

def get_input():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        if filename != '-':
            return open(filename)
    return sys.stdin

def read_arrangement(inp):
    answer = int(inp.readline()) - 1
    for i in xrange(answer):
        inp.readline()
    answer_row = inp.readline().strip().split(" ")
    for i in xrange(answer+1,4):
        inp.readline()
    return answer_row

if __name__ == "__main__":
    src = get_input()
    cases = int(src.readline())
    for i in xrange(1,cases+1):
        first = set(read_arrangement(src))
        second = set(read_arrangement(src))
        inter = first.intersection(second)

        if len(inter) is 0:
            print "Case #%s: Volunteer cheated!" % i
        elif len(inter) is 1:
            print "Case #%s: %s" % (i, inter.pop())
        else:
            print "Case #%s: Bad magician!" % i