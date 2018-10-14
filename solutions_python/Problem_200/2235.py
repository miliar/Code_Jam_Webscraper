
def solve():
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
    for index in range(1, t + 1):
        # n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
        # print("Case #{}: {} {}".format(i, n + m, n * m))
        # check out .format's specification for more formatting options
        in_data = [s for s in input().split(" ")]
        m = in_data[0]
        number = list(m)
        length = len(number)
        if length == 1:
            output = 'Case #%d: %s' % (index, number[0])
            print(output)
            continue
        cnt = 0
        old = -1
        for i in number:
            if cnt == 0:
                cnt += 1
                old = int(i)
                continue

            if int(i) < old:
                for k in range(cnt, length):
                    number[k] = '9'
                for k in range(cnt - 1, -1, -1):
                    if k == 0 or number[k - 1] < number[k]:
                        number[k] = str(int(number[k]) - 1)
                        break;
                    number[k] = '9'
            old = int(i)
            cnt += 1
        result = "".join(number)
        result = int(result)
        output = 'Case #%d: %d' % (index, result)
        print(output)

solve()