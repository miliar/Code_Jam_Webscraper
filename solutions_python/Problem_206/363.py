
if __name__ == "__main__":
    T = input()

    for i in range(T):
        D, N = map(int, raw_input().split())
        H = []
        for _ in range(N):
            H.append(map(int, raw_input().split()))

        times = []
        for k, s in H:
            times.append((D - k) / (s + .0))

        print "Case #%d: %.8f" % (i + 1, D / max(times))

