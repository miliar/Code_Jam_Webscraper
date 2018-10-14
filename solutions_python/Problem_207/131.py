#!/bin/python3

T = int(input().strip())
for test in range(T):
    N, R, O, Y, G, B, V = [int(x) for x in input().split()]
    # print(N, R, O, Y, G, B, V)
    ans = ''
    if ((B < O) or (R < G) or (Y < V)):
        ans = 'IMPOSSIBLE'
    elif ((B == O) and (B != 0)):
        if ((R > 0) or (Y > 0)):
            ans = 'IMPOSSIBLE'
        else:
            ans = ('BO' * B)
    elif ((R == G) and (R != 0)):
        if ((B > 0) or (Y > 0)):
            ans = 'IMPOSSIBLE'
        else:
            ans = ('RG' * R)
    elif ((Y == V) and (Y != 0)):
        if ((R > 0) or (B > 0)):
            ans = 'IMPOSSIBLE'
        else:
            ans = 'YV' * Y
    else:
        counts = {}
        counts['B'] = B - O
        counts['R'] = R - G
        counts['Y'] = Y - V
        li = [(x, counts[x]) for x in counts]
        srtli = sorted(li, key=lambda x: x[1])
        if (srtli[2][1] > (srtli[0][1] + srtli[1][1])):
            ans = 'IMPOSSIBLE'
        else:
            while counts[srtli[2][0]] > 0:
                ans += srtli[2][0]
                counts[srtli[2][0]] -= 1
                if counts[srtli[1][0]] >= counts[srtli[0][0]]:
                    ans += srtli[1][0]
                    counts[srtli[1][0]] -= 1
                else:
                    ans += srtli[0][0]
                    counts[srtli[0][0]] -= 1
            while (counts[srtli[1][0]] > 0) or (counts[srtli[0][0]] > 0):
                if counts[srtli[1][0]] == counts[srtli[0][0]]:
                    if ans[-1] == srtli[1][0]:
                        ans += srtli[0][0]
                        counts[srtli[0][0]] -= 1
                    else:
                        ans += srtli[1][0]
                        counts[srtli[1][0]] -= 1
                elif counts[srtli[1][0]] > counts[srtli[0][0]]:
                    ans += srtli[1][0]
                    counts[srtli[1][0]] -= 1
                else:
                    ans += srtli[0][0]
                    counts[srtli[0][0]] -= 1
            # now insert O, G, Y
            counts['O'] = O
            counts['G'] = G
            counts['V'] = V
            place = {'B': 'O', 'R': 'G', 'Y': 'V'}
            ogvans = ''
            for c in ans:
                while counts[place[c]] > 0:
                    ogvans += c
                    ogvans += place[c]
                    counts[place[c]] -= 1
                ogvans += c
            ans = ogvans
    print('Case #%d: %s' % ((test + 1), ans))
