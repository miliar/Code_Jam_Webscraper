
if __name__ == "__main__":
    T = input()

    for i in range(T):
        D, N = map(int, raw_input().split())
        H = []
        max_time = 0
        for _ in range(N):
            k, s = map(int, raw_input().split())
            max_time = max(max_time, (D - k) / (s + .0))

        print "Case #%d: %.8f" % (i + 1, D / max_time)

