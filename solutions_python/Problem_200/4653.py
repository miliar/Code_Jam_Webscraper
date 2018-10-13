from eulerlib import *

def last_tidy(m):
    for n in range(m, 0, -1):
        if is_tidy(n):
            return n

def is_tidy(n):
    n = str(n)

    last_d = int(n[0])
    change = set()

    for c in n[1:]:
        if 1 in change:
            return False
        
        current_d, last_d = last_d, int(c)
        value = current_d - last_d

        if value < 0:
            change.add(-1)
        elif value > 0:
            change.add(1)

    return 1 not in change

solutions = []

with open("B-small-attempt0.in") as file:
    i = 1
    for line in file.readlines()[1:]:
        v = int(line)
        last = last_tidy(v)
        solutions.append("Case #" + str(i) + ": " + str(last) + "\n")
        i += 1

with open("B-answers.txt", "w") as file:
    file.writelines(solutions)
