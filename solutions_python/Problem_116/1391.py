UNKNOWN = 'UNKNOWN'
XWON = 'X won'
OWON = 'O won'
DRAW = 'Draw'
INCOMPLETE = 'Game has not completed'

def main():
    T = int(raw_input())
    t = 1
    while t <= T:
        data = []
        data.append(raw_input())
        data.append(raw_input())
        data.append(raw_input())
        data.append(raw_input())

        sequences = []
        sequences.extend(data)
        diag1 = ''
        diag2 = ''
        for i in range(4):
            vertical = ''
            for j in range(4):
                vertical += data[j][i]
            sequences.append(vertical)
            diag1 += data[i][i]
            diag2 += data[i][3-i]
        sequences.append(diag1)
        sequences.append(diag2)

        output = UNKNOWN

        complete = True
        for seq in sequences:
            if '.' in seq:
                complete = False
            else:
                if 'X' not in seq:
                    output = OWON
                    break
                elif 'O' not in seq:
                    output = XWON
                    break

        if output == UNKNOWN:
            if complete:
                output = DRAW
            else:
                output = INCOMPLETE

        print "Case #{}: {}".format(t, output)

        raw_input() # Empty line
        t += 1


if __name__ == "__main__":
    main()