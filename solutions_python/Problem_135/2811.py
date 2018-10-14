import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as inp:
        cases = int(inp.readline())
        for case in range(cases):
            first_answer = int(inp.readline())
            first_arr = [
                map(int, inp.readline().split()),
                map(int, inp.readline().split()),
                map(int, inp.readline().split()),
                map(int, inp.readline().split()),
            ]
            second_answer = int(inp.readline())
            second_arr = [
                map(int, inp.readline().split()),
                map(int, inp.readline().split()),
                map(int, inp.readline().split()),
                map(int, inp.readline().split()),
            ]
            res = set(first_arr[first_answer-1]).intersection(set(second_arr[second_answer-1]))
            print "Case #{}:".format(case+1),
            if len(res) == 1:
                print list(res)[0]
            elif len(res) == 0:
                print "Volunteer cheated!"
            elif len(res) > 1:
                print "Bad magician!"
