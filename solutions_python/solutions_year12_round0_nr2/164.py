surprising_triplets = {i: [] for i in range(31)}
good_triplets = {i: [] for i in range(31)}

def generate_triplets():
    for a in range(11):
        for b in range(11):
            if (abs(a-b) > 2): continue
            for c in range(11):
                if (abs(a-c) > 2): continue
                if (abs(b-c) > 2): continue
                if (abs(a-b) == 2) or (abs(a-c) == 2) or (abs(b-c) == 2):
                    surprising_triplets[a+b+c].append((a, b, c))
                else:
                    good_triplets[a+b+c].append((a, b, c))

def solve(N, S, p, points):
    best = {}

    total = points[0]
    max_s = [max(triplet) for triplet in surprising_triplets[total]]
    max_ns = [max(triplet) for triplet in good_triplets[total]]
    if any(m >= p for m in max_s):
        best[0, 1] = 1
    elif any(m < p for m in max_s):
        best[0, 1] = 0
    if any(m >= p for m in max_ns):
        best[0, 0] = 1
    elif any(m < p for m in max_ns):
        best[0, 0] = 0

    for i in range(1, N):
        total = points[i]
        max_s = [max(triplet) for triplet in surprising_triplets[total]]
        max_ns = [max(triplet) for triplet in good_triplets[total]]
        for s in range(S+1):
            try:
                if any(m >= p for m in max_s):
                    tmp = best[i-1, s] + 1
                elif any(m < p for m in max_s):
                    tmp = best[i-1, s]
                else:
                    tmp = None
                if tmp is not None:
                    try:
                        best[i, s+1] = max(best[i, s+1], tmp)
                    except KeyError:
                        best[i, s+1] = tmp
            except KeyError:
                pass

            try:
                if any(m >= p for m in max_ns):
                    tmp = best[i-1, s] + 1
                elif any(m < p for m in max_ns):
                    tmp = best[i-1, s]
                else:
                    tmp = None
                if tmp is not None:
                    try:
                        best[i, s] = max(best[i, s], tmp)
                    except KeyError:
                        best[i, s] = tmp
            except KeyError:
                pass

    return best[N-1, S]

if __name__ == '__main__':
    generate_triplets()
    T = int(raw_input())
    for X in range(1, T+1):
        numbers = [int(i) for i in raw_input().split(' ')]
        N = numbers[0]
        S = numbers[1]
        p = numbers[2]
        points = numbers[3:]
        print "Case #%d: %s" % (X, solve(N, S, p, points))
