import sys

def test(i):
    ans1 = sys.stdin.readline()
    cards1 = [
        sys.stdin.readline().split(),
        sys.stdin.readline().split(),
        sys.stdin.readline().split(),
        sys.stdin.readline().split()
    ]

    ans2 = sys.stdin.readline()
    cards2 = [
        sys.stdin.readline().split(),
        sys.stdin.readline().split(),
        sys.stdin.readline().split(),
        sys.stdin.readline().split()
    ]

    row1 = cards1[int(ans1) - 1]
    row2 = cards2[int(ans2) - 1]

    cards = []
    for card in row1:
        if card in row2:
            cards.append(card)
    
    print 'Case #%d:' % i,

    if len(cards) == 0:
        print 'Volunteer Cheated!'
    elif len(cards) == 1:
        print cards[0]
    else:
        print 'Bad Magician!'

def main():
    T = sys.stdin.readline()

    for i in range(int(T)):
        test(i + 1)

main()
