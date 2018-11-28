
t = int(raw_input())

for i in range(t):
    n, r, o, y, g, b, v = [int(s) for s in raw_input().split()]
    tmp = n / 2
    if r > tmp or y > tmp or b > tmp:
        print "Case #{0}: IMPOSSIBLE".format(i + 1)
    else:
        num = n
        ans = ""
        last = ""
        while num > 0:
            tmp = "r"
            if last == "":
                if y >= b:
                    if y > r:
                        tmp = "y"
                else:
                    if b > r:
                        tmp = "b"
            elif last == "r":
                if y >= b:
                    tmp = "y"
                else:
                    tmp = "b"
            elif last == "y":
                if r >= b:
                    tmp = "r"
                else:
                    tmp = "b"
            elif last == "b":
                if r >= y:
                    tmp = "r"
                else:
                    tmp = "y"

            num -= 1
            if tmp == "r":
                r -= 1
                ans += "R"
                last = "r"

            if tmp == "y":
                y -= 1
                ans += "Y"
                last = "y"

            if tmp == "b":
                b -= 1
                ans += "B"
                last = "b"

        if ans[0] == ans[-1]:
            ans = ans[:-2] + ans[-1] + ans[-2]

        print "Case #{0}: {1}".format(i + 1, ans)

