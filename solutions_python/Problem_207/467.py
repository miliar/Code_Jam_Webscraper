def getMaxWithPref(last, R, Y, B, PREF):
    m = -1
    if last == 'R':
        m = max(Y, B)
    elif last == 'Y':
        m = max(R, B)
    elif last == 'B':
        m = max(R, Y)
    else:
        m = max(max(R, Y), B)
    if PREF == 'R' and (R == m) and (last != 'R'):
        return 'R'
    if PREF == 'Y' and (Y == m) and (last != 'Y'):
        return 'Y'
    if PREF == 'B' and (B == m) and (last != 'B'):
        return 'B'
    if m == R and (last != 'R') :
        return 'R'
    if m == Y and (last != 'Y'):
        return 'Y'
    if m == B and (last != 'B'):
        return 'B'
    return 'X'


T = int(input())
for tid in range(T):
    N, R, O, Y, G, B, V = [int(x) for x in input().split(' ')]
    result = ''
    bluechain = ''
    yellowchain = ''
    redchain = ''
    if N == 1:
        if R == 1:
            result = 'R'
        if O == 1:
            result = 'O'
        if Y == 1:
            result = 'Y'
        if G == 1:
            result = 'G'
        if B == 1:
            result = 'B'
        if V == 1:
            result = 'V'
    else:
        #blue chain
        if O > B:
            result = 'IMPOSSIBLE'
        elif (O == B) and (O > 0) and (R == 0) and (Y == 0) and (G == 0) and (V == 0):
            result = 'OB' * O
        elif O > 0:
            bluechain = 'BO' * O + 'B'
            B -= O
            O = 0
        #yellow chain
        if V > Y:
            result = 'IMPOSSIBLE'
        elif (V == Y) and (V > 0) and (R == 0) and (B == 0) and (G == 0) and (O == 0):
            result = 'VY' * V
        elif V > 0:
            yellowchain = 'YV' * V + 'Y'
            Y -= V
            V = 0
        #red chain
        if G > R:
            result = 'IMPOSSIBLE'
        elif (G == R) and (G > 0) and (R == 0) and (Y == 0) and (O == 0) and (B == 0):
            result = 'GR' * O
        elif G > 0:
            redchain = 'RG' * G + 'R'
            R -= G
            G = 0
        if result == '':
            # we have just R, Y, B
            #greedy with preference of the first letter:
            PREF = '' # it doesn't matter
            last = ''
            while ((R > 0) or (Y > 0) or (B > 0)):
                letter = getMaxWithPref(last, R, Y, B, PREF)
                if letter == 'X':
                    result = 'IMPOSSIBLE'
                    break
                result += letter
                if letter == 'Y':
                    Y -= 1
                if letter == 'R':
                    R -= 1
                if letter == 'B':
                    B -= 1
                if PREF == '':
                    PREF = letter
                last = letter
            if result[0] == result[len(result)-1]:
                result = 'IMPOSSIBLE'
            if result != 'IMPOSSIBLE':
                if (len(bluechain) > 0):
                    for i, x in enumerate(result):
                        if x == 'B':
                            result = result[:i] + bluechain + result [i+1:]
                if (len(redchain) > 0):
                    for i, x in enumerate(result):
                        if x == 'R':
                            result = result[:i] + redchain + result [i+1:]
                if (len(yellowchain) > 0):
                    for i, x in enumerate(result):
                        if x == 'Y':
                            result = result[:i] + yellowchain + result [i+1:]

    print('Case #{}: {}'.format(tid + 1, str(result)))
