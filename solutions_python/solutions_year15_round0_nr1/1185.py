num_cases = int(raw_input())
for case in range(num_cases):
    row = raw_input().split(" ")
    smax = int(row[0])
    audience = [int(c) for c in list(row[1])]
    ans = 0
    for i in range(1, smax + 1):
        if audience[i - 1] < i:
            ans += i - audience[i - 1]
            audience[i - 1] = i
        audience[i] += audience[i - 1]
    print "Case #%d: %d" % (case + 1, ans)
    
