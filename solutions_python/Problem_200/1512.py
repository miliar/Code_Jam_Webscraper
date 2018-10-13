import sys

def fill9(N, f):
    for i in range(f, len(N)):
        N[i] = 9

def max_tidy(N):
    for i in range(len(N) - 1, 0, -1):
        if N[i] < N[i-1]:
            N[i-1] -= 1
            fill9(N, i)

    return N



if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for t in range(1, T+1):
        N = sys.stdin.readline().strip()
        N = [int(d) for d in N]
        N = max_tidy(N)
        N = int("".join([str(d) for d in N]))
        print("Case #%s: %s" % (t, N))
