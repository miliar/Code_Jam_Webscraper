import sys

T = int(sys.stdin.readline())


def possible():
    row_num = int(sys.stdin.readline())
    row = []
    for i in range(1, 5):
        if i == row_num:
            row = map(int, sys.stdin.readline().split())
        else:
            sys.stdin.readline()
    return set(row)


for test_case in range(1, T+1):
    result = possible().intersection(possible())
    print "Case #" + str(test_case) + ":",
    if len(result) < 1:
        print "Volunteer cheated!"
    if len(result) == 1:
        print result.pop()
    if len(result) > 1:
        print "Bad magician!"


