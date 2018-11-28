# python A.py < input/A_test.in > output/A_test.out
# python A.py < input/A_small.in > output/A_small.out
# python A.py < input/A_large.in > output/A_large.out

def copy_state(rows):
    rows2 = []
    for r in rows:
        rows2.append(r)

def f(rows):
    # pass1: fill downward (by copying)
    for i in range(1, len(rows)):
        row = rows[i]
        for j in range(len(row)):
            if row[j] == "?":
                row[j] = rows[i - 1][j]

    # pass2: fill upward
    for i in range(len(rows) - 2, -1, -1):
        for j in range(len(rows[i])):
            if rows[i][j] == "?":
                rows[i][j] = rows[i + 1][j]

    # pass3: fill right
    for ci in range(1, len(rows[0])):
        for ri in range(len(rows)):
            if rows[ri][ci] == "?":
                rows[ri][ci] = rows[ri][ci - 1]

    # pass4: fill left
    for ci in range(len(rows[0]) - 2, -1, -1):
        for ri in range(len(rows)):
            if rows[ri][ci] == "?":
                rows[ri][ci] = rows[ri][ci + 1]

    return(rows)

if __name__ == "__main__":
    test_count = int(raw_input())
    for i in range(test_count):
        r, c = [int(x) for x in raw_input().split()]
        rows = []
        for j in range(r):
            rows.append(list(raw_input()))

        print("Case #%d:" % (i + 1))
        ans = f(rows)
        for row in ans:
            print("".join(row))


"""
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each begins with one line with two integers R and C. Then, there are R more lines of C characters each, representing the cake. Each character is either an uppercase English letter (which means that your assistant has already added that letter to that cell) or ? (which means that that cell is blank).



"""
