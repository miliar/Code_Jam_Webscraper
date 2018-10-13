import sys

def solve(N, K):
    fake_point = 0

    copy_n = N[:]
    copy_k = K[:]

    while N:
        if N[0] < K[0]:
            del N[0]
            del K[-1]
        else:
            fake_point += 1
            del N[0]
            del K[0]

    real_point = 0

    while copy_n:
        if copy_k[-1] > copy_n[0]:
            index = next(i for i, v in enumerate(copy_k) if v > copy_n[0])
            del copy_k[index]
            del copy_n[0]
        else:
            del copy_n[0]
            del copy_k[0]
            real_point += 1

    return fake_point, real_point

def main():
    for tc in range(1, int(sys.stdin.readline()) + 1):
        sys.stdin.readline()
        N = sorted([float(x) for x in sys.stdin.readline().split()])
        K = sorted([float(x) for x in sys.stdin.readline().split()])
        fake, real = solve(N, K)
        print("Case #%s: %d %d" % (tc, fake, real))

if __name__ == '__main__':
    main()
