import sys
import math

def solve():
    N, P = map(int, sys.stdin.readline().rstrip().split())

    R = map(int, sys.stdin.readline().rstrip().split())

    Qs = []

    for ing in range(N):
        packs = map(int, sys.stdin.readline().rstrip().split())

        # For each one, find the lowest number of servings it supports,
        # highest number of servings it supports, and sort at the end

        ing_q = []
        for pack in packs:
            min_servings = int(math.ceil(pack * 10 * 1.0 / (11 * R[ing])))
            max_servings = int(math.floor(pack * 10 * 1.0 / (9 * R[ing])))
            ing_q.append((max_servings, min_servings))

            assert min_servings * 11 * R[ing] * 1.0 / 10 >= pack
            assert max_servings * 9 * R[ing] * 1.0 / 10 <= pack

        ing_q = sorted(ing_q)
        Qs.append(ing_q)

    #for ing in Qs:
    #print ing
    kits_seen = 0

    # Check if heads form a kit
    # If not, pop smallest endpoint
    Q_indices = [0 for i in range(N)]
    while True:
        #print Q_indices
        min_upper, max_lower = Qs[0][Q_indices[0]]
        earliest = 0
        for i in range(1, N):
            upper, lower = Qs[i][Q_indices[i]]
            if upper < min_upper:
                min_upper = upper
                earliest = i
            if lower > max_lower:
                max_lower = lower

        if max_lower <= min_upper:
            #print max_lower

            kits_seen += 1
            for i in range(N):
                assert max_lower >= Qs[i][Q_indices[i]][1]
                assert max_lower <= Qs[i][Q_indices[i]][0]
                Q_indices[i] += 1
                if Q_indices[i] >= P:
                    return kits_seen
        else:
            Q_indices[earliest] += 1
            if Q_indices[earliest] >= P:
                return kits_seen


def main():
    T = int(sys.stdin.readline().rstrip())
    for t in range(1, T+1):
        answer = solve()
        print 'Case #{}: {}'.format(t, answer)

if __name__ == "__main__":
    main()
