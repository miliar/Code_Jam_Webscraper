import sys

T = int(sys.stdin.next())
message = "Case #{0}: {1}"

case = 1
while case <= T:
    row1 = int(sys.stdin.next().strip())
    set1 = [sys.stdin.next().strip() for i in range(4)]

    row2 = int(sys.stdin.next().strip())
    i = 0
    set2 = [sys.stdin.next().strip() for i in range(4)]

    row1 = set(set1[row1-1].split())
    row2 = set(set2[row2-1].split())

    choices = row1.intersection(row2)
    if len(choices) == 0:
        print message.format(case, "Volunteer cheated!")
    elif len(choices) > 1:
        print message.format(case, "Bad magician!")
    else: 
        print message.format(case, choices.pop())
    case += 1
