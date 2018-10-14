import sys

def solve(row1, cards1, row2, cards2):
    row1 = cards1[row1 - 1]
    row2 = cards2[row2 - 1]
    card = set(row1) & set(row2)
    l = len(card)
    if l == 1:
        return card.pop()
    if l > 1:
        return "Bad magician!"
    return "Volunteer cheated!"

def main():
    T = int(sys.stdin.readline())
    for t in range(T):
        data = []
        row1 = int(sys.stdin.readline())
        cards1 = [map(int, sys.stdin.readline().split()) for r in range(4)]
        row2 = int(sys.stdin.readline())
        cards2 = [map(int, sys.stdin.readline().split()) for r in range(4)]
        result = solve(row1, cards1, row2, cards2)
        print "Case #%d: %s" % (t + 1, result)

if __name__ == '__main__':
    main()
