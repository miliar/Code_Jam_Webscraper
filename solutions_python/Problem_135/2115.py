def intersection(b1, b2):
    return [val for val in b1 if val in b2]

def row_number(n):
    for i in xrange(n):
        line = f.readline()

    for i in xrange(4 - n):
        f.readline()

    return line[:len(line) - 1].split(" ")

def output(ans, i):
    out.write("Case #" + str(i + 1) + ": ")
    if (len(ans) == 0):
        out.write("Volunteer cheated!\n")
    if (len(ans) == 1):
        out.write(ans[0] + "\n")
    if (len(ans) > 1):
        out.write("Bad magician!\n")

def guess(i):
    row1 = int(f.readline())
    possible_cards1 = row_number(row1)
    row2 = int(f.readline())
    possible_cards2 = row_number(row2)
    ans = intersection(possible_cards1, possible_cards2)
    output(ans, i)

f = open('input.txt', 'r')
out = open('output.txt', 'w')

T = int(f.readline())

for i in xrange(T):
    guess(i)

f.close()
out.close()
