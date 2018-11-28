import sys

f_in = open("A-small-attempt0.in", "r")
f_out = open("magic.out", "w")

size = int(f_in.readline())

for (n, case) in enumerate(range(size)):
    ans1 = int(f_in.readline())

    for r in range(4):
        row = f_in.readline()
        if r == ans1 - 1:
            row1 = set([int(x) for x in row.split()])

    ans2 = int(f_in.readline())
    for r in range(4):
        row = f_in.readline()
        if r == ans2 - 1:
            row2 = set([int(x) for x in row.split()])

    inter = row1.intersection(row2)

    if len(inter) == 1:
        final_answer = str(inter.pop())
    elif len(inter) == 0:
        final_answer = "Volunteer cheated!"
    else:
        final_answer = "Bad magician!"

    f_out.write("Case #" + str(n + 1) + ": " + final_answer + "\n")

f_in.close()
f_out.close()