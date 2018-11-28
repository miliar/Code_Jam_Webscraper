import sys

def nontidy_val(x):
    prevx = 9
    val = 0
    idx = 1
    while x > 0:
        if x % 10 > prevx:
            return val
        prevx = x % 10
        x = x // 10
        val += prevx * idx
        idx *= 10
    return None


def solve(data):
    n = int(data)
    val = nontidy_val(n)
    while val is not None:
        n -= (val+1)
        val = nontidy_val(n)
    return n


def solve_inputs(inputs):
    cnt = int(inputs[0])
    for i in range(cnt):
        print("Case #{}: {}".format(i + 1, solve(inputs[i+1])))


def main():
    solve_inputs(sys.stdin.readlines())


if __name__ == '__main__':
    main()