from math import ceil
tests = int(raw_input())
for _ in range(1, tests+1):
    D = int(raw_input())
    plates = map(int, raw_input().split())
    plates.sort(reverse=True)
    B = [0]*D
    threshold = plates[0]
    ans = pos = 0
    for i in range(plates[0], -1, -1):
        #print 'i', i 
        ma = ma2 = 0
        for j in range(D):
            n = int(ceil(plates[j]*1./(B[j]+1)))
            #print 'n', n
            if ma < n:
                ma2 = ma
                ma = n
                pos = j
            elif ma2 < n:
                ma2 = n
            #print 'j', j, 'ma',ma, 'ma2', ma2,'pos', pos
        n = int(ceil(plates[pos]*1./(B[pos]+2)))
        #print 'n', n
        if max(n,ma2) + 1 + ans < threshold:
            threshold = ans+1 + max(ma/2 + ma%2,ma2);
        ans += 1
        B[pos] += 1
        #print 'ans', ans, 'threshold', threshold
        #print 'B', B 
    print 'Case #' + str(_) + ': ' + str(int(threshold)) 




