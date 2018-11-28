#!/usr/bin/env python

from collections import defaultdict

fin = open("2.in", "r")
fout = open("2.out", "w")

T = int(fin.readline())
for t in range(T):
    print str(t+1)
    N, R, O, Y, G, B, V = map(int, fin.readline().split())

    ans = []
    B -= O
    Y -= V
    R -= G
    if B < 0 or Y < 0 or R < 0 or R + B < Y or R + Y < B or B + Y < R:
        ans = "IMPOSSIBLE"

    if ans != "IMPOSSIBLE":
        ry = R + Y - B
        rb = R + B - Y
        by = B + Y - R
        if ry % 2 == 1 and rb % 2 == 1 and by % 2 == 1:
            ry -= 1
            rb -= 1
            by -= 1
            ans = ["Y", "R", "B"]
        if ry > 0:
            add = ["Y", "R"] * (ry / 2)
            if len(ans) == 0:
                ans = add
            else:
                for i in range(len(ans)):
                    if ans[i] == "R":
                        ans = ans[:i+1] + add + ans[i+1:]
                        break
                    elif ans[i] == "Y":
                        ans = ans[:i] + add + ans[i:]
                        break
        if rb > 0:
            add = ["B", "R"] * (rb / 2)
            if len(ans) == 0:
                ans = add
            else:
                for i in range(len(ans)):
                    if ans[i] == "R":
                        ans = ans[:i+1] + add + ans[i+1:]
                        break
                    elif ans[i] == "B":
                        ans = ans[:i] + add + ans[i:]
                        break
        if by > 0:
            add = ["Y", "B"] * (by / 2)
            if len(ans) == 0:
                ans = add
            else:
                for i in range(len(ans)):
                    if ans[i] == "B":
                        ans = ans[:i+1] + add + ans[i+1:]
                        break
                    elif ans[i] == "Y":
                        ans = ans[:i] + add + ans[i:]
                        break
        if O > 0:
            add = ["O", "B"] * O
            if len(ans) <= 1:
                ans = add
            else:
                for i in range(len(ans)):
                    if ans[i] == "B":
                        ans = ans[:i+1] + add + ans[i+1:]
                        break
        if V > 0:
            add = ["V", "Y"] * V
            if len(ans) <= 1:
                ans = add
            else:
                for i in range(len(ans)):
                    if ans[i] == "Y":
                        ans = ans[:i+1] + add + ans[i+1:]
                        break
        if G > 0:
            add = ["G", "R"] * G
            if len(ans) <= 1:
                ans = add
            else:
                for i in range(len(ans)):
                    if ans[i] == "R":
                        ans = ans[:i+1] + add + ans[i+1:]
                        break

    if ans != "IMPOSSIBLE":
        ans = "".join(ans)
    fout.write("Case #" + str(t+1) + ": " + str(ans) + "\n")
