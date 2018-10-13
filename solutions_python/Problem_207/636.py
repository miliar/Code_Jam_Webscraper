import sys
import operator
sys.setrecursionlimit(1000000)

COLORS = ['R', 'O', 'Y', 'G', 'B', 'V']
SHARED_COLORS = {('R', 'O'),
                 ('O', 'Y'),
                 ('Y', 'G'),
                 ('G', 'B'),
                 ('B', 'V'),
                 ('V', 'R')}

POSSIBLE_COLORS = {'R': set("YGB"), "O": set("GBV"),
                   'Y': set('BVR'), "G": set("VRO"),
                   'B': set("RYO"), "V": set("OYG")}


def parseCase(fin):
    line = next(fin).strip()
    pony = map(int, line.split(' '))
    return pony


def colorsAreShared(color1, color2):
    return color1 == color2 or (color1, color2) in SHARED_COLORS


def pickMaxColor(ponies, prevColor, nextColor):
    possibleColors = ponies.keys()
    if prevColor is not None:
        possibleColors &= POSSIBLE_COLORS[prevColor]
    if nextColor is not None:
        possibleColors &= POSSIBLE_COLORS[nextColor]

    possiblePonies = ( (color, num) for (color, num) in ponies.items() if color in possibleColors )
    maxColor, maxPonies = max(possiblePonies, key=operator.itemgetter(1))
    if maxPonies == 0:
        return None
    else:
        return maxColor


def pickColors(N, ponies, startColor):
    colors = [startColor]
    ponies[startColor] -= 1
    prevColor = startColor
    nextColor = None
    for i in range(1, N):
        if i == N-1:
            nextColor = colors[0]
        prevColor = pickMaxColor(ponies, prevColor, nextColor)
        if prevColor is None:
            return None

        colors.append(prevColor)
        ponies[prevColor] -= 1
    return colors


def isPossible(ponies):
    return ponies['R'] <= ponies['Y'] + ponies['B'] and \
           ponies['Y'] <= ponies['B'] + ponies['R'] and \
           ponies['B'] <= ponies['R'] + ponies['Y']


def check(N, colors, ponies):
    assert len(colors) == N
    assert colors[0] != colors[-1]
    for(a, b) in zip(colors, colors[1:]):
        assert a!=b
    for color, num in ponies.items():
        assert num == colors.count(color), "Wrong colors count: "+color


def solve(N, R, O, Y, G, B, V):
    ponies = {'R':R, 'O':O, 'Y':Y, 'G':G, 'B':B, 'V':V}
    if isPossible(ponies):
        for color, num in ponies.items():
            if num>0:
                stalls = pickColors(N, ponies.copy(), color)
                if stalls is not None:
                    check(N, stalls, ponies)
                    return "".join(stalls)
    else:
        return "IMPOSSIBLE"


def main(filenameIn, filenameOut):
    with open(filenameIn, 'rt') as fin, open(filenameOut, 'wt') as fout:
        line = next(fin).strip()
        count = int(line)
        for i in range(count):
            N, R, O, Y, G, B, V = parseCase(fin)
            answer = solve(N, R, O, Y, G, B, V)
            fout.write("Case #{}: {}\n".format(i+1, answer))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
