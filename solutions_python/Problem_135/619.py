import sys

def get_row():
    row = int(raw_input())
    value = set()

    for i in xrange(4):
        numbers = map(int, raw_input().split())

        if row == i + 1:
            value = set(numbers)

    return value

def solve_case(test_case):
    numbers = get_row() & get_row()
    print "Case #%d: %s" % (test_case,
        "Volunteer cheated!" if not numbers else
        "Bad magician!" if len(numbers) > 1 else
        str(numbers.pop()))

for test_case in xrange(1, int(raw_input()) + 1):
    solve_case(test_case)
    sys.stdout.flush()
