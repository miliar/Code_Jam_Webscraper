import math

with open('input.in', 'r') as f:
    with open('output.out', 'w') as out:
        t = int(f.readline())

        for i in range(1, t+1):
            s = f.readline().strip()
            while not s:
                s = f.readline().strip
            length = len(s)
            num = int(s)
            j = 0
            while j < length - 1:
                digit = int(s[length - j - 1])
                next = int(s[length - j - 2])
                if digit < next:
                    sub = int(s[length - j - 1:])
                    num -= sub + 1  # turns into a 9
                    s = str(num)
                    length = len(s)
                    if num == 0:
                        break
                    if j > 0:
                        j -= 2
                j += 1
            out.write("Case #" + str(i) + ": " + s + "\n")
