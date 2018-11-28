import sys

f = sys.stdin

def solve(answer_1, cards_1, answer_2, cards_2):
    possible_1 = cards_1[answer_1 - 1]
    possible_2 = cards_2[answer_2 - 1]

    possible   = [card for card in possible_1 if card in possible_2]

    if len(possible) == 1:
        return possible[0]
    elif len(possible) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"


tests = int(f.readline())

for i in range(1,tests+1):
    answer_1 = int(f.readline().strip())
    cards_1  = [map(int, f.readline().split()) for _ in range(4)]

    answer_2 = int(f.readline().strip())
    cards_2  = [map(int, f.readline().strip().split()) for _ in range(4)]
    print "Case #%d:" % i, solve(answer_1, cards_1, answer_2, cards_2)


