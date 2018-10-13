
def solve(n, p, gs):
    buckets = [0] * p
    for item in gs:
        mod = item % p
        buckets[mod] += 1
    fresh_only = buckets[0]
    if p == 2:
        fresh_only += (buckets[1] + 1) / 2
    if p == 3:
        mini = min(buckets[1], buckets[2])
        fresh_only += mini
        buckets[1] -= mini
        buckets[2] -= mini
        fresh_only += (buckets[1] + 2) / 3
        fresh_only += (buckets[2] + 2) / 3
    return fresh_only

t = input()

for i in range(1, t + 1):
    n,p = map(int, raw_input().strip().split())
    gs = map(int, raw_input().strip().split())
    print 'Case #{}: {}'.format(i, solve(n, p, gs))
