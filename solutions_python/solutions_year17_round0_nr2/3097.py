import sys


def is_tidy(line):
    stack = list(reversed(map(int, line)))
    if len(stack) == 1:
        return True
    prev = stack.pop()
    while len(stack) > 0:
        next_ = stack.pop()
        if prev > next_:
            return False
        else:
            prev = next_
    return True


def prevtidy(line):
    while True:
        if is_tidy(line):
            return line
        line = str(int(line) - 1)


def minus_one(stack):
    mx = max(stack)
    if mx == 1:
        try:
            stack.pop()
        except:
            pass
        stack[:] = [9] * len(stack)
    else:
        findex = stack.index(mx)
        stack[findex] -= 1
        stack[findex+1:] = [9]*len(stack[findex+1:])


def solve_case(line):
    if is_tidy(line):
        return line
    stack = list(reversed(map(int, line)))
    if len(stack) == 1:
        return line
    prev = stack.pop()
    out = []
    while len(stack) > 0:
        next_ = stack.pop()
        out.append(prev)
        if prev > next_:
            minus_one(out)
            out.extend([9]*(len(stack)+1))
            break
        else:
            prev = next_
    return ''.join(map(str, out))


def solve(inp, out):
    inp.readline()
    for i, line in enumerate(inp):
        if line.strip():
            result = solve_case(line.strip())
            out.write('Case #%d: %s\n' % (i+1, result))


if __name__ == '__main__':
    solve(sys.stdin, sys.stdout)
