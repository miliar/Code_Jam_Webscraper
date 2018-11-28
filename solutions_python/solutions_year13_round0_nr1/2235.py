import argparse

statuses = (
    "X won",    # (the game is over, and X won)
    "O won",    # (the game is over, and O won)
    "Draw",     # (the game is over, and it ended in a draw)
    "Game has not completed")   # (the game is not over yet)


def read_input(input_file):
    number_of_test_cases = input_file.readline()
    for i in xrange(1, int(number_of_test_cases) + 1):
        data = ''
        for j in xrange(4):
            data += input_file.readline().strip('\n')
        status = compute_status(data)
        print 'Case #%d: %s' % (i, status)
        input_file.readline()


def compute_status(data):
    status = None
    c0, c1, c2, c3 = '', '', '', ''
    for i in xrange(0, 16, 4):
        r = data[i:i + 4]
        status = analyze_sequence(r)
        if status:
            break
        c0 += data[i]
        c1 += data[i+1]
        c2 += data[i+2]
        c3 += data[i+3]

    if not status:
        for c in (c0, c1, c2, c3):
            status = analyze_sequence(c)
            if status:
                break

    if not status:
        d0 = ''
        for i in xrange(0, 16, 5):
            d0 += data[i]
        status = analyze_sequence(d0)

    if not status:
        d1 = ''
        for i in xrange(3, 13, 3):
            d1 += data[i]
        status = analyze_sequence(d1)

    if not status:
        if data.count('.'):
            status = statuses[3]

    if not status:
        status = statuses[2]

    return status


def analyze_sequence(s):
    status = None
    if s.count('T') and s.count('X') == 3:
        status = statuses[0]
    elif s.count('X') == 4:
        status = statuses[0]
    elif s.count('T') and s.count('O') == 3:
        status = statuses[1]
    elif s.count('O') == 4:
        status = statuses[1]
    return status


def one(input_file):
    read_input(input_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=file)
    args = parser.parse_args()
    one(args.input_file)
