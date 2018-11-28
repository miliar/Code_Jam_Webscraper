
def pancake(s, k):
    solveable = set(['-' + (k-1)*'+' + '-', k*'-'])
    moves = 0
    index = 0
    s = list(s)
    while index < len(s):
        if s[index] == '+':
            index += 1
        elif s[index] == '-':
            if index+k > len(s):
                return 'IMPOSSIBLE'
            if index+k < len(s)+1 and ''.join(s[index:index+k]) in solveable:
                index += k
                moves += 1
            elif index+k+1 < len(s)+1 and ''.join(s[index:index+k+1]) in solveable:
                index += k+1
                moves += 2
            else:
                for flip in xrange(index, index+k):
                    if s[flip] == '+':
                        s[flip] = '-'
                    else:
                        s[flip] = '+'
                index += 1
                moves += 1

    return moves

def p(s, k, i, moves, solveable):
    if i == len(s):
        return moves

    if s[i] == '+':
        return p(s, k, i+1, moves, solveable)
    elif s[i] == '-':
        if i+k > len(s):
            return 'IMPOSSIBLE'

        if i+k <= len(s) and ''.join(s[i:i+k]) in solveable:
            return p(s, k, i+k, moves+1, solveable)
        elif i+k+1 <= len(s) and ''.join(s[i:i+k+1]) in solveable:
            return p(s, k, i+k+1, moves+2, solveable)
        else:
            for flip in xrange(i, i+k):
                if s[flip] == '+':
                    s[flip] = '-'
                else:
                    s[flip] = '+'
            return p(s, k, i+1, moves+1, solveable)


def f(s, k):
    solveable = set(['-' + (k-1)*'+' + '-', k*'-'])
    return p(list(s), k, 0, 0, solveable)



# print f('---+-+++-', 5)
#

t = int(raw_input())
for i in xrange(1, t+1):
    s, k = raw_input().split(' ')
    k = int(k)
    print 'Case #{}: {}'.format(i, pancake(s, k))
