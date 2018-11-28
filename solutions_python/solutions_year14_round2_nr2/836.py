
import sys
RL = lambda: sys.stdin.readline().strip()
IA = lambda: map(int, RL().split(" "))
LA = lambda: map(long, RL().split(" "))

T = int(sys.stdin.readline())

for CASE in range(T):
    A,B,K = IA()
    answer = 0
    for i in range(A):
        for j in range(B):
            if i & j < K:
                answer+=1
    print "Case #%d: %s" % (CASE+1, answer)

