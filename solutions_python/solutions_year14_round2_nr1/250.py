import math

def isPossible(words, d):
    chars = ''
    for n in range(0,N):
        newchars = words[n][0]
        count = 0
        l = []
        for c in words[n]:
            if c != newchars[-1]:
                l.append(count)
                newchars += c
                count = 1
            else:
                count += 1
        l.append(count)
        d.append(l)
        if chars == '':
            chars = newchars
        elif chars != newchars:
            return False
    return True

def calculate(d):
    count = 0
    for i in range(0,len(d[0])):
        q = []
        for n in range(0,N):
            q.append(d[n][i])
        q.sort()
        m = math.floor(len(q)/2)
        for v in range(0,len(q)):
            count += math.fabs(q[v] - q[m])
    return math.floor(count)

with open('A-large.in', 'r') as fin:
    with open('output', 'w') as fout:
        T = int(fin.readline())
        for t in range(1,T+1):
            N = int(fin.readline())
            words = []
            for n in range(0,N):
                words.append(fin.readline().strip())

            d = []
            if isPossible(words, d):
                r = calculate(d)
            else:
                r = 'Fegla Won'

            fout.write('Case #{}: {}\n'.format(t, r))
