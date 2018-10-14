import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

n = int(raw_input())
for i in range(n):
    s, p = raw_input().split()
    ppl = [int(x) for x in p]
    answ = 0
    total = ppl[0]
    for k in range(1, int(s)+1):
        if ppl[k] != 0:
            if total < k:
                answ += k-total
                total += k-total
            total += ppl[k]
    print "Case #"+str(i+1)+": "+str(answ)