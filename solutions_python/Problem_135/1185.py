import sys
import collections

def readPosition(inp):
    ans = int(inp.readline())
    field = collections.defaultdict(dict)
    for y in xrange(4):
        data = [int(x) for x in inp.readline().split()]
        for x, card in enumerate(data):
            field[y][x] = card
    return ans, field

def main():
    with open(sys.argv[1], 'r') as inp:
        T = int(inp.readline())
        for t in xrange(T):
            ans1, field1 = readPosition(inp)
            ans2, field2 = readPosition(inp)

            cards = set(field1[ans1 - 1].values()) & set(field2[ans2 - 1].values())
            if not cards:
                result = 'Volunteer cheated!'
            elif len(cards) > 1:
                result = 'Bad magician!'
            else:
                result = str(list(cards)[0])
            print 'Case #%s: %s' % (t + 1, result)

if __name__ == '__main__':
    main()
