import fileinput

remaining = -1
current = 0

for line in fileinput.input():
    if remaining == -1:
        remaining = int(line)
    else:
        current += 1
        n= int(line)

        x = n
        while x > 0:
            y = str(x)
            if y == ''.join(sorted(y)):
                print 'Case #{0}: {1}'.format(current, y)
                break

            new_x = ''
            prev = 0
            for z in y:
                if int(z) < prev:
                    new_x = new_x[:-1] + str(int(new_x[-1]) - 1)
                    new_x += ('9' * (len(y) - len(new_x)))
                    break
                else:
                    new_x += z
                    prev = int(z)

            x = str(int(new_x))
        
        remaining -= 1
        if remaining == 0: break