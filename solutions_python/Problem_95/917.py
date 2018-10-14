f = open('A-small.in')
g = open('A-small-output.in', 'w')
T = int(f.readline())
X = 1
alphabet = ['y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q']
while T > 0:
    line = f.readline()[0:-1]
    i = 0
    S = ''
    while i < len(line):
        if line[i] not in alphabet:
            S += line[i]
        else:
            S += alphabet[ord(line[i]) - ord('a')]
        i += 1
    if X != 1:
        g.write('\n')
    g.write('Case #{}: {}'.format(X, S))
    T -= 1
    X += 1
f.close()
g.close()
