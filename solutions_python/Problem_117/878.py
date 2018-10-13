filename = "B-large"

def solve(rows, case):
    cols = []

    for i in range(len(rows)):
        row = rows[i]
        for j in range(len(row)):
            char = row[j]
            if len(cols) <= j:
                cols.append([])
            cols[j].append(char)

    for i in range(len(rows)):
        row = rows[i]

        # If all chars equal, it is the best
        if len(row) == row.count(row[0]):
            continue

        for j in range(len(row)):
            char = row[j]

            col_ok = True
            row_ok = True

            for colchar in cols[j]:
                if (colchar > char):
                    col_ok = False

            for rowchar in row:
                if (rowchar > char):
                    row_ok = False

            # Row or column must be OK
            if row_ok == False and col_ok == False:
                return False

    return True

fi = open(filename + ".in", "r")
fo = open(filename + ".out", "w")

cases = int(fi.readline())

for case in range(cases):
    mnline = fi.readline().replace("\n", "")
    mnvalues = mnline.split(" ", 1)
    m = int(mnvalues[0])

    rows = []
    for i in range(m):
        line = fi.readline().replace("\n", "")
        row = [int(num) for num in line.split(" ")]
        rows.append(row)

    output = "YES" if solve(rows, case + 1) else "NO"
    result = "Case #%d: %s" % (case + 1, output)
    print(result)
    fo.write(result + "\n")

fi.close()
fo.close()