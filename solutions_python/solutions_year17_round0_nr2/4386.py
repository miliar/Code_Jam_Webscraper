# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    if n > 9:
        myStr = list(str(n))
        prev = 0
        current = 1
        changed = 0

        while current < len(myStr):
            if myStr[prev] > myStr[current]:
                changed = 1
                while current < len(myStr):
                    myStr[current] = '9'
                    current += 1
                while prev >= 0:
                    if prev == 0 and myStr[prev] == '1':
                        myStr.pop(0)
                        break
                    elif myStr[prev] == '1':
                        myStr[prev] = '9'
                    elif myStr[prev] > '1':
                        myStr[prev] = str(int(myStr[prev])-1)
                        break
                    prev -= 1

            if changed == 0:
                prev = current
                current += 1
            else:
                current = 1
                prev = 0
                changed = 0

        n = int(''.join(myStr))


    print("Case #{}: {}".format(i, n))
# check out .format's specification for more formatting options
