def is_tidy(N):
    prev = 0
    for d in N:
        digit = int(d)
        if digit < prev:
            return False
        prev = digit
    return True


def solution(N):
    ret = list(str(N))
    for i in range(1, len(ret) + 1):
        if is_tidy(ret):
            break
        else:
            ret[-i] = "9"
            ret[-i - 1] = str(int(ret[-i - 1]) - 1)
    return int("".join(ret))


if __name__ == '__main__':
    with open("input.txt") as fp:
        lines = fp.readlines()

    T = int(lines[0])
    for i in range(T):
        n = int(lines[1+i])
        print("Case #%d: %d" % (i+1, solution(n)))
