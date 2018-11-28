#!/usr/bin/python3

fin = open("D-small-0.in", "r")
fout = open("D-small-0.out", "w")

valid3 = {(2, 3), (3, 3), (3, 4)}
valid4 = {(3, 4), (4, 4)}

def solve():
    x, r, c = list(map(int, fin.readline().split()))
    if r > c:
        r, c = c, r
    if x == 1:
        fout.write("GABRIEL\n")
    elif x == 2:
        if r * c % 2 == 0:
            fout.write("GABRIEL\n")
        else:
            fout.write("RICHARD\n")
    elif x == 3:
        if (r, c) in valid3:
            fout.write("GABRIEL\n")
        else:
            fout.write("RICHARD\n")
    else:
        if (r, c) in valid4:
            fout.write("GABRIEL\n")
        else:
            fout.write("RICHARD\n")

T = int(fin.readline())

for i in range(1, T + 1):
    fout.write("Case #%d: " % i)
    solve()

fin.close()
fout.close()
