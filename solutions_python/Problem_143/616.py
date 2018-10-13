

for case in range(int(raw_input())):
    A, B, K = map(int, raw_input().split())
    cnt = 0
    for i in range(A):
        for j in range(B):
            if i&j < K:
                cnt += 1 
                
    print "Case #%d: %d" % (case+1, cnt)