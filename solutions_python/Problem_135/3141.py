from __future__ import division
from sys import argv

def solve(a1, cards1, a2, cards2):
    suspects = cards1[a1-1].intersection(cards2[a2-1])
    if len(suspects) == 1:
        return suspects.pop()
    elif len( suspects) > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"

def main(lines):
    T = int(lines.pop(0))
    case = 1
    for t in range(T):
        a1 = int(lines.pop(0))
        cards1 = [set(int(card) for card in lines.pop(0).split()) for i in range(4)]
        a2 = int(lines.pop(0))
        cards2 = [set(int(card) for card in lines.pop(0).split()) for i in range(4)]
        print "Case #%d: %s" % (case, solve(a1, cards1, a2, cards2))
        case += 1

if __name__ == '__main__':
    main(open(argv[1]).read().split('\n'))