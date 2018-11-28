import fileinput

def read_input():
    # gets next line from the file specified as argument or stdin
    # useful to debug within PyCharm, because you can't redirect stdin :-(
    # first time, initialize a function attribute (it's like a static local function in C++)
    # that will keep state across invocations
    if not hasattr(read_input, 'input'):
        read_input.input = fileinput.input()
    return read_input.input.next().strip()


def untidy_position(n):
    last_digit = '0'
    for i,d in enumerate(n):
        if d < last_digit:
            return i
        last_digit = d
    return -1


assert -1 == untidy_position('8')
assert -1 == untidy_position('123')
assert -1 == untidy_position('555')
assert -1 == untidy_position('224488')
assert untidy_position('20')
assert untidy_position('321')
assert untidy_position('495')
assert untidy_position('999990')


def solve(N):
    p = untidy_position(N)

    if p == -1:
        return N
    else:
        return solve(str(int(N[:p])-1)) + ('9' * (len(N)-p))


if __name__ == "__main__":
    T = int(read_input())
    # sys.stderr.write("%d\n" % (T,))
    for i in xrange(1, T+1):
        N = read_input()
        solution = str(int(solve(N)))
        print("Case #%d: %s" % (i, solution))


