input = open('D-small-attempt0.in', 'r')
output = open('D-small-attempt0.out', 'w')
t = int(input.readline().rstrip())
for test in range(t):
    x, r, c = map(int, input.readline().rstrip().split())
    ans = "ANYBODY"
    if r * c % x != 0:
        ans = "RICHARD"
    elif x < 3:
        ans = "GABRIEL"
    elif x == 3:
        if r * c == 3:
            ans = "RICHARD"
        else:
            ans = "GABRIEL"
    elif x == 4:
        if r > 2 and c > 2:
            ans = "GABRIEL"
        else:
            ans = "RICHARD"
    output.write("Case #" + str(test + 1) + ": " + ans + "\n")

input.close()
output.close()