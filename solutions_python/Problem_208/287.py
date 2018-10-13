import sys

if __name__ == "__main__":
    T = input()

    for i in range(T):
        N, Q = map(int, raw_input().split())
        E_S = []
        for _ in range(N):
            E_S.append(map(int, raw_input().split()))

        A = []
        for _ in range(N):
            A.append(map(int, raw_input().split()))

        if Q != 1:
            raise

        U, V = map(int, raw_input().split())

        times = [sys.maxint] * N
        for j in range(N - 1):
            idx = j
            ej, sj = E_S[j]
            time = 0 if j == 0 else times[j - 1]
            while idx < N- 1 and ej >= A[idx][idx + 1]:
                time += (A[idx][idx + 1] / (sj + .0))
                times[idx] = min(times[idx], time)
                ej -= A[idx][idx + 1]
                idx += 1

        print "Case #%d: %.8f" % (i + 1, times[N - 2])

