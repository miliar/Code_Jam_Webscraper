T = int(raw_input())
for case in range(1,T+1):
    A,B,K = map(int,raw_input().split())
    counter = 0
    for i in range(A):
        for j in range(B):
            if i&j < K:
               counter += 1
    print 'Case #' + str(case) + ': ' + str(counter) 
