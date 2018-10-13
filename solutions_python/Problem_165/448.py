
with open('A-small-attempt0.in') as f:
    lines = [line.strip() for line in open('A-small-attempt0.in')]

file1 = open("Asmallout.txt", "w")

t = int(lines[0])

tm = t + 1

for i in range(1,tm):

    l = map(int, lines[i].split(" "))
    r = l[0]
    c = l[1]
    w = l[2]
    if w == 1:
        ans= r*c

    elif w == r * c or (w == r*c -1):
        ans = r * c

    elif c == 1:
        ans = 1

    elif c == 3:
        ans = 3

    elif c == 4:
        if w ==2:
            ans = 3
        else:
            ans = 4

    elif c == 5:
        if w == 2 or w == 3:
            ans = 4
        elif w == 4:
            ans = 5

    elif c == 6:
        if w == 2 or w == 3:
            ans = 4
        elif w == 4:
            ans = 5
        elif w == 5:
            ans = 6

    elif c == 7:
        if w == 2 or w == 3 or w==4:
            ans = 5
        elif w == 5:
            ans = 6

    elif c == 8:
        if w == 2 or w == 3 or w==4:
            ans = 5
        elif w == 5:
            ans = 6
        elif w== 6:
            ans = 7
        elif w == 7:
            ans = 8

    elif c == 9:
        if w == 2 or w == 4 or w == 5:
            ans = 6
        elif w == 3:
            ans = 5
        elif w == 6:
            ans = 7
        elif w == 7:
            ans = 8

    elif c == 10:
        if w == 2 or w == 3  or w ==4 or w == 5:
            ans = 6
        elif w == 6:
            ans = 7
        elif w == 7:
            ans = 8
        elif w == 8:
            ans = 9

    file1.write("Case  #%d: %d\n" % (i, ans))

file1.close()