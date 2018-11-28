"""gcj"""

def solve_a():
    """solveA"""

    def check(table, c, i0, j0, di, dj):
        """check"""
        for k in xrange(4):
            i = i0 + k * di
            j = j0 + k * dj
            if table[i][j] == "T":
                continue
            if table[i][j] != c:
                return False
        return True

    def check2(table, c):
        """check2"""

        for i in xrange(4):
            if check(table, c, i, 0, 0, 1):
                return True
        for j in xrange(4):
            if check(table, c, 0, j, 1, 0):
                return True
        if check(table, c, 0, 0, 1, 1):
            return True
        if check(table, c, 0, 3, 1, -1):
            return True
        return False

    with open("A-large.in") as in_file:
        with open("out", "w+") as out_file:
            num_cases = int(in_file.readline())

            for case_index in xrange(num_cases):
                table = []
                for _ in xrange(4):
                    table.append(in_file.readline())
                in_file.readline()

                result = "Draw"
                has_winner = False
                if (not has_winner) and check2(table, "X"):
                    result = "X won"
                    has_winner = True
                if (not has_winner) and check2(table, "O"):
                    result = "O won"
                    has_winner = True
                if not has_winner:
                    for i in xrange(4):
                        has_moves = False
                        for j in xrange(4):
                            if table[i][j] == ".":
                                has_moves = True
                                result = "Game has not completed"
                                break
                        if has_moves:
                            break

                out_file.write(
                    "Case #" + str(case_index + 1) + ": " + result + "\n"
                )

def main():
    """main"""
    solve_a()

if __name__ == "__main__":
    main()