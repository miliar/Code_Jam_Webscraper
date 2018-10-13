
import sys

def get_choices():
    row = int(sys.stdin.readline())
    # Read lines preceeding row number
    for _ in xrange(row - 1):
        sys.stdin.readline()
    line = [int(x) for x in sys.stdin.readline().split()]
    # Read lines following row number
    for _ in xrange(row, 4):
        sys.stdin.readline()
    return set(line)

if __name__ == '__main__':

    num_cases = int(sys.stdin.readline())

    for i in xrange(1, num_cases + 1):
        row1 = get_choices()
        row2 = get_choices()
        values = row1 & row2
        num_values = len(values)
        if num_values == 0:
            print 'Case #' + str(i) +': Volunteer cheated!'
        elif num_values > 1:
            print 'Case #' + str(i) + ': Bad magician!'
        else:
            print 'Case #' + str(i) + ':', values.pop()