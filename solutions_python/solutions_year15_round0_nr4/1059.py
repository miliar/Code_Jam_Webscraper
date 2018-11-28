#! python3

def main():
    with open("D-small-attempt0.in") as in_file:
        with open("D-small.out", "w") as fout:
            cases = int(in_file.readline())
            for x in range(cases):
                line = in_file.readline().replace('\n', '').split(' ')
                X = int(line[0])
                R = int(line[1])
                C = int(line[2])
                winner = 'GABRIEL'
                if X >= 7:
                    winner = 'RICHARD'
                elif R * C % X is not 0:
                    winner = 'RICHARD'
                elif R < X and C < X:
                    winner = 'RICHARD'
                elif X >= 4 and (R is 2 or C is 2):
                    winner = 'RICHARD'
                elif X is 6 and (R is 3 or C is 3):
                    winner = 'RICHARD'
                else:
                    for y in range(1, X + 1):
                        length = y
                        width = X - y + 1
                        if (length > R or width > C) and (width > R or length > C):
                            winner = 'RICHARD'

                fout.write("Case #{0}: {1}\n".format(x + 1, winner))

if __name__ == "__main__":
    main()
