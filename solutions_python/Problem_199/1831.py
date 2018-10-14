# Google Code Jam 2017 Round 1
# Problem A. Oversized Pancake Flipper

def flips(S, K):
    changes = 0
    new = [i for i in S]
    for i in range(len(S) - K + 1):
        if new[i] == '-':
            changes += 1
            for j in range(i, i + K):
                if new[j] == '+':
                    new[j] = '-'
                else:
                    new[j] = '+'
    if '-' in new:
        return 'IMPOSSIBLE'
    return str(changes)

def pancakes():
    f = open('pancakes.txt', 'r')
    g = open('flips.txt', 'w')
    line = 0
    for i in f:
        if line == 0:
            T = int(i)
            line = 1
        else:
            S = ''
            K = ''
            space = False
            for j in i:
                if j == ' ':
                    space = True
                else:
                    if space:
                        K += j
                    else:
                        S += j
            g.write('Case #' + str(line) + ': ')
            g.write(flips(S, int(K)) + (line != T)*'\n')
            line += 1
    f.close()
    g.close()
        
