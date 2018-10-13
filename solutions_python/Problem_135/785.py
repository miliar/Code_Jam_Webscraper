import sys

def get_row_guesses():
    row = int(sys.stdin.readline().strip()) - 1
    guesses = None
    for i in range(4):
        data = [int(x) for x in sys.stdin.readline().strip().split(' ')]
        if i == row:
            guesses = set(data)

    return guesses

def process_case():
    first_guess = get_row_guesses()
    second_guess = get_row_guesses()

    guesses = first_guess.intersection(second_guess)
    
    if len(guesses) == 0:
        return 'Volunteer cheated!'
    elif len(guesses) == 1:
        return str(guesses.pop())
    else:
        return 'Bad magician!'

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        result = process_case()
        print 'Case #%d: %s' % (i + 1, result)

if __name__ == '__main__':
    main()
