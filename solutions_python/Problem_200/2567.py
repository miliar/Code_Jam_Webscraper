import sys

def num2digits(num):
    l = []
    while num > 0:
        l.insert(0, num % 10)
        num /= 10
    return l

def digits2num(digits):
    num = 0
    for digit in digits:
        num = num * 10 + digit
    return num

# Returns a tuple (tidy, index)
# where index is the first position that fails the tidy test.
def is_tidy(digits):
    for i in range(len(digits)-1):
        if digits[i] > digits[i+1]:
            return (False, i+1)

    return (True, 0)

def find_tidy_slow(num):
    while not is_tidy(num2digits(num))[0]:
        num -= 1
    return num

# Attempt to make `digits` tidy.
# Note that it may not actually be tidy...
def make_tidy(digits, index):
    # All digits from the index onwards will be 9
    for i in range(index, len(digits)):
        digits[i] = 9

    # Preceding index (if it exists) needs to be reduced by 1
    assert (index > 0)
    digits[index - 1] -= 1

def find_tidy_fast(num):
    digits = num2digits(num)
    # First, find the first (most significant) position where the test fails
    tidy, where = is_tidy(digits)

    # We should only need to run this loop len(digits) times at maximum.
    while not tidy:
        # Adjust it so that it is tidy *from that point onwards*
        make_tidy(digits, where)

        tidy, where = is_tidy(digits)

    return digits2num(digits)

def test_tidy():
    # Test lower numbers
    for i in range(10000):
        assert(find_tidy_fast(i) == find_tidy_slow(i))


if __name__ == '__main__':
    # Parse the test file and generate output
    # Discard first line
    sys.stdin.readline()

    case = 1
    for line in sys.stdin:
        line = line.strip()
        if line:
            num = int(line)
            result = find_tidy_fast(num)
            print "Case #%d: %s" % (case, result)
            case += 1


