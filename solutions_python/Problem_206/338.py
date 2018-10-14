# Zolmeister

T = int(raw_input())

def get_time(horse, D):
    K, S = horse
    return (D - K) / float(S)

for t in xrange(T):
    D, N = map(int, raw_input().split())
    horses = []
    for l in xrange(N):
        horses.append(map(int, raw_input().split()))

    horses = sorted(horses)
    max_time = 0
    for horse in horses:
        max_time = max(max_time, get_time(horse, D))

    max_speed = D / max_time
    print 'Case #{}: {}'.format(t + 1, max_speed)
