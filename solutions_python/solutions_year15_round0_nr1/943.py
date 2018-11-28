import sys

def input():
    T = int(sys.stdin.readline())
    for i in range(1,T+1,1):
        S, ppl = sys.stdin.readline().split()
        S = int(S)
        print "Case #{}: {}".format(i,extra(S,ppl))

def extra(S,ppl):
    current = 0
    required = 0
    for i,cnt in enumerate(ppl):
        current += int(cnt)
        if current <= i:
            required += i - current + 1
            current += i - current + 1
    return required

input() 