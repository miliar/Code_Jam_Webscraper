
def parse(fn):
    results = []
    f = open(fn)
    output = open(fn + '.output', 'w')
    # skip first line
    next(f)
    case = 1
    for line in f:
        N = int(line)
        result = getLast(N)
        print(result)
        print('Case #{}: {}'.format(case, result), file=output)
        case += 1
    f.close()
    output.close()


def isTidy(number):
    S = str(number)
    if len(S) == 1:
        return True

    for i in range(1, len(S)):
        if S[i-1] > S[i]:
            return False

    return True



def getLast(N):
    digits = str(N)
    if len(digits) == 1:
        return N

    for i in range(1, len(digits)):
        if digits[i-1] > digits[i]:
            mess = int(digits[:i+1])
            rest = digits[i+1:]
            rest = ''.join('9' for _ in rest)
            return getLast(int(str(mess - 1) + rest))
    return N

# getLast(111111111111111110)
parse('B-large.in')

