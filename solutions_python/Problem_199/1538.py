import sys

def flip(s):
    newS = ''
    for c in s:
        if c == '-':
            newS = newS + '+'
        else:
            newS = newS + '-'
    return newS

def flips(s, k):
    fliped = 0
    for i in range(len(s) - k + 1):
        if s[i] == '-':
            s = s[:i] + flip(s[i: i+k]) + s[i+k:]
            fliped += 1

    done = True
    for i in range(len(s) - k + 1, len(s)):
        c = s[i]
        if c == '-':
            done = False
            break

    if done:
        return fliped
    else:
        return "IMPOSSIBLE"

n = int(input())
for i in range(n):
    line = input()
    li = line.split();
    s = li[0]
    k = int(li[1])

    '''
    unflipped = 0
    for c in s:
        if c == '-':
            unflipped += 1
    '''

    print('Case #' + str(i + 1) + ': ', end='')
    print(flips(s, k))


        


    
