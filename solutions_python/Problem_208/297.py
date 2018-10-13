import sys

def compute(N, mhara_horse, A):
    times = [sys.maxint] * N
    for j in range(N - 1):
        idx = j
        ej, sj = mhara_horse[j]
        time = 0 if j == 0 else times[j - 1]
        while idx < N- 1 and ej >= A[idx][idx + 1]:
            time += (A[idx][idx + 1] / (sj + .0))
            times[idx] = min(times[idx], time)
            ej -= A[idx][idx + 1]
            idx += 1

    return times[N - 2]

if __name__ == "__main__":
    tests = input()

    for i in range(tests):
        N, queries = map(int, raw_input().split())

        mhara_horse = []
        for _ in range(N):
            mhara_horse.append(map(int, raw_input().split()))

        A = []
        for _ in range(N):
            A.append(map(int, raw_input().split()))

        _, _ = map(int, raw_input().split())

        print "Case #%d: %.10f" % (i + 1, compute(N, mhara_horse, A))

