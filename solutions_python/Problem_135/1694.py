#!/usr/bin/env python

from collections import deque

FILENAME = 'A-small-attempt1.in'

def load_board(q):
    result = deque()

    max = 4
    for x in range(0, max):
        item = q.popleft()

        result.append(item.split())

    return result

def load_from_file():
    result = None

    with open(FILENAME) as f:
        result = [line.rstrip('\n') for line in f]

    return deque(result)

def main():
    data = load_from_file()
    number_of_cases = int(data.popleft())

    for x in range(0, number_of_cases):
        history = {}
        found = 0
        winner = -1
        chosen = int(data.popleft())

        board = load_board(data)
        row = board[chosen-1]

        for i in range(0, len(row)):
            history[row[i]] = True

        chosen = int(data.popleft())

        board = load_board(data)
        row = board[chosen-1]

        for i in range(0, len(row)):
            if row[i] in history:
                found += 1
                winner = row[i]

        if found > 1:
            print "Case #" + str(x+1) + ": " + "Bad magician!"
        elif found == 1:
            print "Case #" + str(x+1) + ": " + str(winner)
        elif found == 0:
            print "Case #" + str(x+1) + ": " + "Volunteer cheated!"



if __name__ == "__main__":
    main()
