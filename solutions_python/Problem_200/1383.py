import sys
import math

def existViolations(digits):
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            return True
    return False

def smallest_tidy_num_lt(x):
    x = x.strip()
    revDigits = map(lambda x: int(x), list(x))[::-1]

    for i in range(len(revDigits) - 1):
        # look for a violation
        if revDigits[i] < revDigits[i + 1]:
            for j in range(i):
                revDigits[j] = 9
            revDigits[i] = 9
            revDigits[i + 1] = revDigits[i + 1] - 1
            break

    digits = revDigits[::-1]
    strDigits = map(lambda x: str(x), digits)
    ret = "".join(strDigits)

    if existViolations(digits):
        ret = smallest_tidy_num_lt(ret)

    return ret

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        case = 0
        for line in f:
            if case == 0:
                case += 1
                continue
            args = line.split(" ")
            print "Case #%s: %s" % (case, int(smallest_tidy_num_lt(args[0])))
            case += 1

