import sys

def maxmin(n, k, d):
    if (n, k) not in d:
        part = (n - 1) // 2
        plus = (n - 1) % 2 != 0
        if k == 0:
            d[(n, k)] = (part + plus, part)
        else:
            part_k = (k - 1) // 2
            plus_k = (k - 1) % 2 != 0
            if plus_k:
                d[(n, k)] = maxmin(part, part_k, d)
            else:
                d[(n, k)] = maxmin(part + plus, part_k, d)
    return d[(n, k)]

def solve(data):
    n, k = map(int, data.split())
    return "{} {}".format(*maxmin(n, k-1, {0: 0}))

def solve_inputs(inputs):
    cnt = int(inputs[0])
    for i in range(cnt):
        print("Case #{}: {}".format(i + 1, solve(inputs[i+1])))


def main():
    solve_inputs(sys.stdin.readlines())

if __name__ == '__main__':
	main()