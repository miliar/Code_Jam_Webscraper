# Google Code Jam 2017 Round 1B
# Problem B. Stable Neigh-bors

def arrange(N, R, Y, B):
    if N == 1:
        if R == 1:
            return 'R'
        if Y == 1:
            return 'Y'
        return 'B'
    if 2*max(R, Y, B) > N:
        return 'IMPOSSIBLE'
    result = ''
    if R == max(R, Y, B):
        current = 'R'
    elif Y == max(R, Y, B):
        current = 'Y'
    else:
        current = 'B'
    for i in range(N):
        result += current
        if current == 'R':
            R -= 1
            if Y >= B:
                current = 'Y'
            else:
                current = 'B'
        elif current == 'Y':
            Y -= 1
            if R >= B:
                current = 'R'
            else:
                current = 'B'
        else:
            B -= 1
            if R >= Y:
                current = 'R'
            else:
                current = 'Y'
    if result[0] == result[-1]:
        return result[:-2] + result[-1] + result[-2]
    return result

def stable():
    f = open('stable.txt', 'r')
    g = open('horses.txt', 'w')
    line = 0
    for i in f:
        if line == 0:
            T = int(i)
            line = 1
        else:
            spaces = 0
            N = ''
            R = ''
            Y = ''
            B = ''
            for j in i:
                if j == ' ':
                    spaces += 1
                else:
                    if spaces == 0:
                        N += j
                    elif spaces == 1:
                        R += j
                    elif spaces == 3:
                        Y += j
                    elif spaces == 5:
                        B += j
            N = int(N)
            R = int(R)
            Y = int(Y)
            B = int(B)
            g.write('Case #' + str(line) + ': ')
            g.write(arrange(N, R, Y, B))
            g.write((T != line)*'\n')
            print line, N, R, Y, B
            line += 1
    f.close()
    g.close()
