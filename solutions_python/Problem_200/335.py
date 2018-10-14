def decr(s, m):
    return s[:m] + str(int(s[m])-1) + s[m+1:]


def put9(s, m):
    return s[:m] + "9" + s[m+1:]


t = int(input())
for a0 in range(t):
    n = input()

    intn = int(n)
    last_dig = -1
    ans = ""

    need_fix = False

    if len(n) == 1:
        print("Case #" + str(a0 + 1) + ": " + n)

    else:
        binary = True
        for d in n:
            if d not in "01":
                binary = False
                break

        if binary:
            print("Case #" + str(a0 + 1) + ": " + "9"*(len(n)-1))

        else:
            for d in n:
                dig = int(d)
                if last_dig <= dig:
                    ans += str(dig)
                    last_dig = dig
                else:
                    need_fix = True
                    break

            if need_fix:
                #print(ans)
                i = len(ans)-1
                d = ans[i]
                done = False
                while i >= 1:
                    if ans[i-1] != d:
                        ans = decr(ans, i)
                        done = True
                        #print("done", ans)
                        break
                    ans = put9(ans, i)
                    i -= 1
                    d = ans[i]
                if not done:
                    ans = decr(ans, 0)

            while int(ans) < intn:
                ans += "9"

            while ans[0] == "0":
                ans = ans[1:]

            if int(ans) > intn:
                ans = ans[:-1]

            print("Case #" + str(a0+1) + ": " + ans)
