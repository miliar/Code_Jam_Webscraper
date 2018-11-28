from collections import defaultdict

def minimum_minutes(pancakes):
    counts = defaultdict(int)
    max_p = 0
    for p in pancakes:
        counts[p] += 1
        max_p = max(p, max_p)

    min_minutes = max_p
    elapsed = 0
    for i in range(max_p, -1, -1):
        min_minutes = min(elapsed + i, min_minutes)
        if counts[i] == 0:
            continue
        x,y = i//2, i-i//2
        counts[x] += counts[i]
        counts[y] += counts[i]
        elapsed += counts[i]
            
    return min_minutes

def minimum_minutes(pancakes):
    m = max(pancakes)
    if m <= 2:
        return m
    i = pancakes.index(m)
    pancakes = pancakes[:i] + pancakes[i+1:] + [m//2, m-m//2]
    return min(m, 1+minimum_minutes(pancakes))

cache = {}
def minimum_minutes(pancakes):
    k = tuple(sorted(pancakes))
    if k in cache:
        return cache[k]
    m = max(pancakes)
    if m <= 2:
        return m
        
    i = pancakes.index(m)
    possibilities = []
    possibilities.append([x-1 for x in pancakes if x > 1])
    p2 = pancakes[:i] + pancakes[i+1:]
    for j in range(1, m//2+1):
        possibilities.append(p2+[j,m-j])
    cache[k] = 1 + min(map(minimum_minutes, possibilities))
    return cache[k]
    

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        raw_input()
        pancakes = [int(a) for a in raw_input().split()]
        print "Case #%d: %d" % (i, minimum_minutes(pancakes))
        
    
