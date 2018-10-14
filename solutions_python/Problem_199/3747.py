#!/usr/bin/python3

def flipAt(s, k, startIndex):
    for i in range(startIndex, startIndex+k):
        if s[i] == '+':
            s[i] = '-'
        else:
            s[i] = '+'

def pushRight(s, k):
    steps = 0
    for i in range(len(s)-k+1):
        if s[i] == '-':
            flipAt(s, k, i)
            steps += 1
    return steps

def allFliped(s):
    for c in s:
        if c == '-':
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    skArray = []
    for i in range(t):
        inp = input()
        s = list(inp.split()[0])
        k = int(inp.split()[1])
        skArray.append((s,k))

    for (i,(s,k)) in enumerate(skArray):
        steps = pushRight(s, k)
        if allFliped(s):
            print('Case #' + str(i+1) + ': ' + str(steps))
        else:
            print('Case #' + str(i+1) + ': IMPOSSIBLE')
