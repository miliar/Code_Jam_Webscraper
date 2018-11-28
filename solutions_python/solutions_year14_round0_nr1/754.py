# Magic Trick


def perform_magic(ans1, card1, ans2, card2):
    set1 = set(card1[ans1 - 1])
    set2 = set(card2[ans2 - 1])
    possible_cards = set1.intersection(set2)
    if len(possible_cards) == 0:
        print('Volunteer cheated!')
    elif len(possible_cards) == 1:
        print(possible_cards.pop())
    else:
        print('Bad magician!')


def read_cards():
    cards = []
    for i in range(4):
        row = input().split()
        cards.append([int(i) for i in row])
    return cards


def main():
    n_cases = int(input())
    for i in range(1, n_cases + 1):
        print('Case #{}: '.format(i), end='')
        ans1 = int(input())
        card1 = read_cards()
        ans2 = int(input())
        card2 = read_cards()
        perform_magic(ans1, card1, ans2, card2)


if __name__ == '__main__':
    main()
