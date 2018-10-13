t = int(raw_input())

for i in range(t):
    d, n = map(int, raw_input().split())
    counts = []
    for j in range(n):
        k, s = map(int, raw_input().split())
        dist = d -k 
        if dist <= 0:
            continue
        
        counts.append(float(dist)/float(s))

    mini = max(counts)

    print "Case #{}: {}".format(i+1, d/mini)
