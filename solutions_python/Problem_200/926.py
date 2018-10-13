import sys

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
NbTests = int(input())  # read a line with a single integer
lsN = []
for i in range(NbTests):
    n = int(sys.stdin.readline().replace('\n', ''))
    lsN.append(n)

def isTidy(N):
    culotte = str(N)
    for i in range(len(culotte) -1):
        if culotte[i] > culotte[i + 1]:
            return False
    return True

def lastTidy(N):
    rep = N
    while(not isTidy(rep)):
        rep -= 1
    return rep

for i in range(1, NbTests + 1):
    rep = lastTidy(lsN[i - 1])
    print("Case #{}: {}".format(i, rep))
