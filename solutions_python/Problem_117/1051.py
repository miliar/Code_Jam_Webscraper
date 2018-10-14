import numpy as np
import sys

data = [line.strip() for line in file(sys.argv[1])]
cases = int(data[0])

case = 1
index = 1
while case < cases + 1:
    rows, cols = map(int, data[index].split(" "))
    lawn = np.zeros(shape = (rows, cols), dtype = int)
    for i in range(1, rows + 1):
        lawn[i - 1] = np.array(map(int, data[index + i].split(" ")))

    valid = True
    for i in range(0, rows):
        for j in range(0, cols):
            h = lawn[i, j]
            vertical = lawn[:, j]
            horizontal = lawn[i, :]
            valid = np.size(np.where(vertical > h)) == 0 or np.size(np.where(horizontal > h)) == 0

            if not valid:
                break
        if not valid:
            break
    if not valid:
        print 'Case #%s: NO' % case
    else:
        print 'Case #%s: YES' % case

    index += (rows + 1)
    case += 1
