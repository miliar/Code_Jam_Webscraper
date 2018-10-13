#! python3

DATA_FILE = "B-small-attempt0"

def main():
    with open(DATA_FILE + ".in") as in_file:
        with open(DATA_FILE + ".out", "w") as fout:
            cases = int(in_file.readline())
            for x in range(cases):
                line = in_file.readline().replace('\n', '')
                N, R, O, Y, G, B, V = [int(n) for n in line.split()]
                placed = []
                if R > 0:
                    placed.append('R')
                    R -= 1
                elif Y > 0:
                    placed.append('Y')
                    Y -= 1
                elif B > 0:
                    placed.append('B')
                    B -= 1
                possible = True
                for i in range(N - 1):
                    if placed[-1] == 'R':
                        if G > 0:
                            placed.append('G')
                            G -= 1
                        elif Y > 0 and B > 0:
                            if max(Y, B) == Y:
                                placed.append('Y')
                                Y -= 1
                            else:
                                placed.append('B')
                                B -= 1
                        elif Y > 0:
                            placed.append('Y')
                            Y -= 1
                        elif B > 0:
                            placed.append('B')
                            B -= 1
                    elif placed[-1] == 'Y':
                        if V > 0:
                            placed.append('V')
                            V -= 1
                        elif R > 0 and B > 0:
                            if max(R, B) == R:
                                placed.append('R')
                                R -= 1
                            else:
                                placed.append('B')
                                B -= 1
                        elif B > 0:
                            placed.append('B')
                            B -= 1
                        elif R > 0:
                            placed.append('R')
                            R -= 1
                    elif placed[-1] == 'B':
                        if O > 0:
                            placed.append('O')
                            O -= 1
                        elif Y > 0 and R > 0:
                            if max(Y, R) == Y:
                                placed.append('Y')
                                Y -= 1
                            else:
                                placed.append('R')
                                R -= 1
                        elif R > 0:
                            placed.append('R')
                            R -= 1
                        elif Y > 0:
                            placed.append('Y')
                            Y -= 1
                    elif placed[-1] == 'O':
                        if B > 0:
                            placed.append('B')
                            B -= 1
                    elif placed[-1] == 'G':
                        if R > 0:
                            placed.append('R')
                            R -= 1
                    elif placed[-1] == 'V':
                        if Y > 0:
                            placed.append('Y')
                            Y -= 1
                    if len(placed) != i + 2:
                        possible = False
                        break

                if placed[-1] == 'R':
                    if not (placed[0] == 'Y' or placed[0] == 'B' or placed[0] == 'G'):
                        possible = False
                elif placed[-1] == 'Y':
                    if not (placed[0] == 'R' or placed[0] == 'B' or placed[0] == 'V'):
                        possible = False
                elif placed[-1] == 'B':
                    if not (placed[0] == 'Y' or placed[0] == 'R' or placed[0] == 'O'):
                        possible = False
                elif placed[-1] == 'O':
                    if not placed[0] == 'B':
                        possible = False
                elif placed[-1] == 'G':
                    if not placed[0] == 'R':
                        possible = False
                elif placed[-1] == 'V':
                    if not placed[0] == 'Y':
                        possible = False

                if possible:
                    fout.write("Case #{0}: {1}\n".format(x + 1, ''.join(placed)))
                else:
                    fout.write("Case #{0}: {1}\n".format(x + 1, 'IMPOSSIBLE'))


if __name__ == "__main__":
    main()
