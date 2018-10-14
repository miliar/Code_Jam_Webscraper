import sys

sys.stdin.readline()
for t, s in enumerate(sys.stdin, 1):
    tokens = s.split()
    x, r, c = int(tokens[0]), int(tokens[1]), int(tokens[2])
    if x == 1:
        possible = True
    elif x == 2:
        possible = r * c % 2 == 0
    elif x == 3:
        possible = r * c % 3 == 0 and r * c >= 6
    else:
        possible = r * c % 4 == 0 and r * c >= 12
    sys.stdout.write("Case #{}: {}\n".format(t, "GABRIEL" if possible else "RICHARD"))
