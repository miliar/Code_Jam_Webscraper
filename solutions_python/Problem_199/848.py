file = "A-large.in"

def count_flips(S, K):
    pancakes = list(S)
    count = 0
    while pancakes:
        if not pancakes:
            return count
        elif pancakes[0] == '+':
            pancakes.pop(0)
        elif len(pancakes) < K:
            return 'IMPOSSIBLE'
        else:
            pancakes = ['-' if p == '+' else '+' for p in pancakes[:K]] + pancakes[K:]
            count += 1
    return count

with open(file) as handle:
    T = int(handle.readline())

    for i in range(T):
        S, K = handle.readline().split(' ')
        K = int(K)


        print 'Case #{}: {}'.format(i + 1, count_flips(S, K))
