from util import *

def check(num, input):
    num_of_row, num_of_col = [ int(x) for x in readline(input).split() ]
    lawn = []
    for _ in xrange(num_of_row):
        lawn.append( [ int(a) for a in readline(input).split() ])

    valid = True

    for row in xrange(num_of_row):
        if not valid:
            break

        for col in xrange(num_of_col):
            if not valid:
                break

            a = lawn[row][col]
            for c in xrange(num_of_col):
                if a < lawn[row][c]:
                    valid = False
                    break

            if valid:
                continue

            valid = True
            for r in xrange(num_of_row):
                if a < lawn[r][col]:
                    valid = False
                    break

    if valid:
        ret = "YES"
    else:
        ret = "NO"

    print "Case #%d: %s" % (num, ret)



if __name__ == '__main__':
    process(check)

