n = int(input())
def check(mp):
    seq = []
    # ->
    for i in range(4):
        seq.append(mp[i])
    # |
    # V
    for j in range(4):
        seq.append([mp[i][j] for i in range(4)])
    # \
    #  v
    seq.append([mp[i][i] for i in range(4)])
    seq.append([mp[3 - i][i] for i in range(4)])
    for s in seq:
        a = set(s)
        if len(a) == 1:
            x = next(iter(a))
            if x != '.':
                return x
        if len(a) == 2 and 'T' in a and '.' not in a:
            for x in a:
                if x != 'T':
                    return x
    return None

for t in range(n):
    mp = []
    for i in range(4):
        while 1:
            s = input()
            if s:
                mp.append(list(s))
                break
    winner = check(mp)
    if winner:
        print('Case #{}: {} won'.format(t + 1, winner))
    else:
        draw = True
        for i in range(4):
            for j in range(4):
                if mp[i][j] == '.':
                    draw = False
                    break
            if not draw: break
        if draw:
            print('Case #{}: Draw'.format(t + 1))
        else:
            print('Case #{}: Game has not completed'.format(t + 1))
