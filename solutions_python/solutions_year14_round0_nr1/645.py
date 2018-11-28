BAD_STRING = "Bad magician!"
CHEATER_STRING = "Volunteer cheated!"
ROWS = 4

def main():
    T = int(raw_input())
    first_cards = [None] * ROWS
    second_cards = [None] * ROWS
    for t in xrange(T):
        first_pick = int(raw_input())
        get_cards(first_cards)
        second_pick = int(raw_input())
        get_cards(second_cards)
        print "Case #" + str(t+1) + ": " + \
                magic(first_pick, first_cards, second_pick, second_cards)

def get_cards(cards):
    for row in xrange(ROWS):
        cards[row] = [int(x) for x in raw_input().split()]

def magic(pick0, cards0, pick1, cards1):
    choices = []
    for card in cards0[pick0 - 1]:
        for other in cards1[pick1 - 1]:
            if card == other:
                choices.append(card)
    if len(choices) == 0:
        return CHEATER_STRING
    elif len(choices) == 1:
        return str(choices[0])
    else:
        return BAD_STRING


if __name__ == "__main__":
    main()
