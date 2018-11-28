import sys

def fetch_selected_row(f, selection):
    for i in range(1, 5):
        line = f.readline()
        if (i == selection):
            selected_row = [int(card) for card in line.split(' ')]

    return selected_row

def main():
    if len(sys.argv) != 2:
        print('Usage: %s INPUT_FILENAME' % sys.argv[0])
        return 1

    input_file = sys.argv[1]

    f = file(input_file)

    number_of_test_cases = int(f.readline())

    for case in range(1, number_of_test_cases + 1):
        first_selection = int(f.readline())
        first_row = fetch_selected_row(f, first_selection)

        second_seletion = int(f.readline())
        second_row = fetch_selected_row(f, second_seletion)

        possible_cards = list(set(first_row).intersection(set(second_row)))

        if len(possible_cards) == 1:
            print('Case #%d: %d' % (case, possible_cards[0]))
        elif len(possible_cards) > 1:
            print('Case #%d: Bad magician!' % case)
        elif len(possible_cards) == 0:
            print('Case #%d: Volunteer cheated!' % case)

    return 0

if __name__ == '__main__':
    sys.exit(main())

