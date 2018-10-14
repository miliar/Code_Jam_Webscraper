#!usr/bin/env python

filename = 'input.txt'
output = 'result.txt'


def main():
    with open(filename, 'r') as f:
        first_line = f.readline()
       #instances = int(first_line)

        read = False
        first_clue = []
        second_clue = []
        partial = []
        sol = []

        for line in f:
            if line.strip():
                line = line.strip().split(' ')

                if len(line) == 1:
                    read = False
                    for i in range(0, int(line[0]) - 1):
                        next(f)
                elif not read:
                    if first_clue:
                        second_clue = line
                        for card in first_clue:
                            if card in second_clue:
                                partial.append(card)
                        sol.append(partial)
                        first_clue = second_clue = partial = []
                    else:
                        first_clue = line
                    read = True
        make_result(sol)


def make_result(sol):
    cont = 0
    res = ''
    with open(output, 'w') as f:
        for item in sol:
            cont = cont + 1
            if len(item) == 0:
                res = res + 'Case #' + str(cont) + ': Volunteer cheated!'
            elif len(item) == 1:
                res = res + 'Case #' + str(cont) + ': ' + item[0]
            else:
                res = res + 'Case #' + str(cont) + ': Bad magician!'
            res = res + '\n'
        f.write(res[:len(res)-1])


main()
