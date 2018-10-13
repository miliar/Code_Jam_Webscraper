"""Pancakes"""
import fileinput
EMPTY = frozenset('?')

def cutter(rows, handler):
    """Cut the cake"""
    cake = []
    previous_row = None
    backtrack = False
    for _ in range(rows):
        row = list(handler.readline().strip())
        chars = set(row)
        no_empty = chars - EMPTY
        len_chars = len(no_empty)
        if len_chars == 0:
            if previous_row:
                row = previous_row
            else:
                backtrack = True
                row = []
        elif len_chars == 1:
            row = [no_empty.pop()] * len(row)
        elif '?' in chars:
            position = 0
            # Find first char
            while row[position] == '?':
                position += 1
            # Fill in backwards
            row[:position] = [row[position]]*position
            position += 1
            while position < len(row):
                if row[position] == '?':
                    row[position] = row[position-1]
                position += 1

        cake.append(row)
        previous_row = row
        if backtrack and row != []:
            cake[:-1] = [row] * (len(cake) - 1)
            backtrack = False
    return cake

def main():
    """Main Method"""
    handler = fileinput.input()
    appearences = int(handler.readline())
    for case in range(1, appearences+1):
        rows, _ = handler.readline().strip().split()
        print('Case #{case}:'.format(case=case))
        for row in cutter(int(rows), handler):
            print(''.join(row))


if __name__ == '__main__':
    main()
