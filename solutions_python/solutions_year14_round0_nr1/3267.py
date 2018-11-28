def read_cards():
    cards = []
    for i in xrange(4):
        cards.append(map(int, raw_input().split()))
    return cards


def solve(a, acards, b, bcards):
    arow = set(acards[a - 1])
    brow = set(bcards[b - 1])
    card = arow & brow
    if len(card) == 1:
        return list(card)[0]
    elif len(card) > 1:
        return 'Bad magician!'
    else:
        return 'Volunteer cheated!'


if __name__ == '__main__':
    T = int(raw_input())
    for t in xrange(T):
        a = int(raw_input())
        acards = read_cards()
        b = int(raw_input())
        bcards = read_cards()
        answer = solve(a, acards, b, bcards)
        print 'Case #%d: %s' % (t + 1, answer)
