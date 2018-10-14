import sys

in_file = open(sys.argv[1], "r")

out_file = open("output.out", "w")

t = int(in_file.readline())

for i in range(t):
    params = in_file.readline().split(' ')
    x = int(params[0])
    r = int(params[1])
    c = int(params[2])

    ans = "GABRIEL"

    if x > r and x > c:
        ans = "RICHARD"
    elif x > 6:
        ans = "RICHARD"
    elif (r * c) % x != 0:
        ans = "RICHARD"
    else:
        small = min(r, c)
        large = max(r, c)
        if x % 2 == 1 and (x + 1) / 2 > small:
            ans = "RICHARD"
        if x % 2 == 0 and x / 2 > small:
            ans = "RICHARD"
        if x == 4 and small == 2:
            ans = "RICHARD"
        if x == 6 and small == 3:
            ans = "RICHARD"



    out_file.write("Case #" + str(i + 1) + ": " + ans)

    out_file.write("\n")

in_file.close()
out_file.close()
