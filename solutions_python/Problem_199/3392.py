import math
states = {}

def allFlips(S, K, flips):
    global states
    for x in range(len(S) - K + 1):
        flipped = []
        for i in range(len(S)):
            if (x <= i < x + K):
                if (S[i] == '+'):
                    flipped.append('-')
                else:
                    flipped.append('+')
            else:
                flipped.append(S[i])
        newMin = False
        flipped = ''.join(flipped)
        if (flipped in states):
            if states[flipped] > flips:
                newMin = True
            states[flipped] = min(flips, states[flipped])
        else:
            states[flipped] = flips
            newMin = True
        if newMin:
            if flipped != len(S) * '+':
                allFlips(flipped, K, flips + 1)


def solve(S, K):
    global states
    states = {S: 0}
    allFlips(S, K, 1)
    if len(S) * "+" in states:
        return states[len(S)  * '+']
    else:
        return "IMPOSSIBLE"

t = int(input())
for n in range(t):
    inputs = input().split()
    x = solve(inputs[0], int(inputs[1]))
    print("Case #{}: {}".format(n+1, x))
