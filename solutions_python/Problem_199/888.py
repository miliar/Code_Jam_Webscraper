import sys

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
NbTests = int(input())  # read a line with a single integer
lsstring = []
lsLongueur  =[]
for i in range(NbTests):
    n, a = str(sys.stdin.readline()).replace('\n', '').split()
    lsstring.append(str(n))
    lsLongueur.append(int(a))

def action(tanga, K):
    cmpt = 0
    culotte = list(tanga)
    for i in range(max(len(culotte) - K + 1, 0)):
        if culotte[i] == '-':
            cmpt += 1
            for j in range(i, i + K):
                if culotte[j] == '+':
                    culotte[j] = '-'
                else:
                    culotte[j] = '+'
    rep = str(cmpt)
    for c in culotte:
        if c == '-':
            rep = "IMPOSSIBLE"
            break
    return rep

for i in range(1, NbTests + 1):
    rep = action(lsstring[i-1], lsLongueur[i-1 ])
    print("Case #{}: {}".format(i, rep))
