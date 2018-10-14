import sys

def count_subseq(line, needle):
    # memory for memoization
    m = {}  # key = (lineIndex, needleIndex)

    # helpful static values
    LINE_LEN = len(line)
    NEEDLE_LEN = len(needle)

    def f(lineIndex, needleIndex):
        """Computes number of subseq in the remaining line form the remaining
        needle.  Memoized."""
        key = (lineIndex, needleIndex)
        try:
            n = m[key]
        except KeyError:
            # have to compute it - not yet memoized
            n = f_compute(lineIndex, needleIndex)
            m[key] = n

        return n

    def f_compute(lineIndex, needleIndex):
        """Computes f (recursive)."""
        # how many chars of each do we have left?
        needle_left = NEEDLE_LEN - needleIndex
        if needle_left == 0:
            return 1 # match!
        line_left = LINE_LEN - lineIndex

        # shift the needle to start at each of the possible later positions
        # max shift to 0 => tackle the smallest problem first to reduce recursion
        shifts = range(line_left - needle_left, -1, -1)
        n = 0
        c = needle[needleIndex] # the char we're currently trying to match
        for shift in shifts:
            # does this shift match the front of the needle?
            i = lineIndex + shift
            if line[i] == c:
                n += f(i+1, needleIndex + 1) # success; continue from the next char

        return n


    return f(0, 0)  # answer is m[0, 0] so compute it


def main():
    lines = sys.stdin.readlines()
    N = int(lines[0])
    tests = [tc[:len(tc)-1] for tc in lines[1:]] # strip off trailing \n's
    assert(len(tests) == N)

    needle = "welcome to code jam"

    # run each test case
    case_num = 1
    for tc in tests:
        n = count_subseq(tc, needle)
        last_four = n % 10000
        print 'Case #%u: %04u' % (case_num, last_four)
        case_num += 1

main()
