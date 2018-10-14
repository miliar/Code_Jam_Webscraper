import sys
import math
import fractions
Frac = fractions.Fraction

def solve(N, P, R, Q):

    def is_kit(pos):
        qs = [Q[i][j] for i, j in enumerate(pos)]
        lower_bounds = [Frac(10 * qij, 11 * ri) for qij, ri in zip(qs, R)]
        upper_bounds = [Frac(10 * qij, 9 * ri) for qij, ri in zip(qs, R)]
        lower_bound = math.ceil(max(lower_bounds))
        upper_bound = math.floor(min(upper_bounds))
        return lower_bound <= upper_bound

    def advance(pos):
        qs = [Q[i][j] for i, j in enumerate(pos)]
        min_i = min(range(N), key=lambda i: Frac(qs[i], R[i]))
        pos[min_i] += 1
        if pos[min_i] == P:
            return False
        return True

    def advance_all(pos):
        for i in range(N):
            pos[i] += 1
            if pos[i] == P:
                return False
        return True

    for q in Q:
        q.sort()

    pos = [0] * N
    kit_count = 0
    while True:
        if is_kit(pos):
            qs = [Q[i][j] for i, j in enumerate(pos)]
            # print(f"kit: " + ", ".join(map(str, qs)))
            kit_count += 1
            if not advance_all(pos):
                break
        else:
            if not advance(pos):
                break

    return kit_count

def main():
    case_count = int(next(sys.stdin))
    for case_number in range(1, case_count + 1):
        N, P = list(map(int, next(sys.stdin).split()))
        R = list(map(int, next(sys.stdin).split()))
        Q = []
        for i in range(N):
            Q.append(list(map(int, next(sys.stdin).split())))
        kit_count = solve(N, P, R, Q)
        print(f"Case #{case_number}: {kit_count}")

if __name__ == "__main__":
    main()
