
from sys import argv


def is_on(n, k):
    i = -1
    while i < k:
        i += 2**n
        if k == i:
            return True
    return False


if __name__ == '__main__':
    input = open(argv[1])
    max_cases = int(input.readline().strip())

    case_n = 0

    for n, k in (x.split(' ') for x in input.readlines()):
        case_n += 1

        print "Case #%s: %s" % (case_n, "ON" if is_on(int(n), int(k)) else "OFF")
        if case_n == max_cases:
            break
    
    
