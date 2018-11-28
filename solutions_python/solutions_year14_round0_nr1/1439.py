import sys

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    possibles = []
    row1 = int(sys.stdin.readline())
    for i in range(1, 5):
        s = sys.stdin.readline().split()
        if i == row1:
            possibles = s

    row2 = int(sys.stdin.readline())
    for i in range(1, 5):
        s = sys.stdin.readline().split()
        if i == row2:
            possibles = [el for el in s if el in possibles]

    if len(possibles) == 0:
        ans = "Volunteer cheated!"
    if len(possibles) > 1:
        ans = "Bad magician!"
    if len(possibles) == 1:
        ans = possibles[0]
    print "Case #" + str(tc) + ": " + ans

