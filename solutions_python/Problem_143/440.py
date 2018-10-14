import sys

def solve(A, B, K):

    count = 0

    for a in range(A):
        for b in range(B):
            result = a & b
            if result < K:
                count += 1
    return count


def main():
    for tc in range(1, int(sys.stdin.readline()) + 1):
        A, B, K = [int(x) for x in sys.stdin.readline().strip().split()]
        print("Case #{}: {}".format(tc, solve(A, B, K)))


if __name__ == '__main__':
    main()
