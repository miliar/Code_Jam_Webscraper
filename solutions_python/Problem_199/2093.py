
def solve():
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        # n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
        # print("Case #{}: {} {}".format(i, n + m, n * m))
        # check out .format's specification for more formatting options
        n, m = [s for s in input().split(" ")]
        m = int(m)
        length = len(n)
        flag = True
        for x in n:
            if x == '-':
                flag = False
                break
        if flag is True:
            output = 'Case #%d: %s' % (i, "0")
            print(output)
            continue
        cnt = 0
        n = list(n)
        flag = True
        result = 0
        for x in n:
            if x == '-':
                n[cnt] = '+'
                for k in range(1, m):
                    # print("i", i)
                    if n[cnt + k] == '-':
                        n[cnt + k] = '+'
                    else:
                        n[cnt + k] = '-'

                # print("pan ", n)
                result += 1
            if (length - cnt == m):
                for y in n[cnt + 1:]:
                    if y ==  '-':
                        flag = False
                        break
                break
            cnt += 1
        if flag is True:
            output = 'Case #%d: %d' % (i, result)
        else:
            output = 'Case #%d: %s' % (i, "IMPOSSIBLE")
        print(output)

solve()