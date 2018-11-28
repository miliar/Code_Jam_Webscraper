import sys
T = int(sys.stdin.readline())

answer = []
answer.append(0)
answer.append(1)
answer.append(3)
for i in range(T):
    (N, K) = map(int, sys.stdin.readline().split())
    if N+1 > len(answer):
        for j in range(len(answer), N+1):
            answer.append(answer[j-1]*2 + 1)
            #print answer
            
    print 'Case #%d: %s' %(i+1, ['OFF', 'ON'][(K + 1) % (answer[N] + 1) == 0])
    
    
