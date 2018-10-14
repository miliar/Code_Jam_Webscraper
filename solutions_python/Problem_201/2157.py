
def solve():
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
    for index in range(1, t + 1):
        # n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
        # print("Case #{}: {} {}".format(i, n + m, n * m))
        # check out .format's specification for more formatting options
        n, m = [int(s) for s in input().split(" ")]
        if n == m:
            output = 'Case #%d: %d %d' % (index, 0, 0)
            print(output)
            continue

        start = 0
        end = n - 1
        y1 = 0
        z1 = 0
        queue = []
        queue.append((start, end))
        for i in range(0, m):
            if len(queue) == 0:
                y1 = 0
                z1 = 0
                break

            max = -2
            max_index = -1
            for iii in range(len(queue)):
                (s1, e1) = queue[iii]
                if e1 - s1 > max:
                    max = e1 - s1
                    max_index = iii

            if max_index < 0:
                break
            (start, end) = queue.pop(max_index)


            if end - start <= 0:
                y1 = 0
                z1 = 0
                continue

            middle = start + int((end - start) / 2)
            y1 = end - middle
            z1 = middle - start
            if z1 >= y1:
                queue.append((start, middle - 1))
                queue.append((middle + 1, end))
            else:
                queue.append((middle + 1, end))
                queue.append((start, middle - 1))
                # print(y1, z1)
                # if y1 < 0:
                #     y1 = 0
                # if z1 < 0:
                #     z1 = 0
        if y1 > z1:
            output = 'Case #%d: %d %d' % (index, y1, z1)
        else:
            output = 'Case #%d: %d %d' % (index, z1, y1)
        print(output)

solve()