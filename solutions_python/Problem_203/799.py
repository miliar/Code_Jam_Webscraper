import sys

    

t = int(sys.stdin.readline())
for t0 in range(t):
    r, c = sys.stdin.readline().split(' ')
    r, c = int(r), int(c)
    cake = []
    for r0 in range(r):
        cake.append([char for char in sys.stdin.readline().strip()])
    for i,row in enumerate(cake):
        if row == ['?']*c:
            ipos = i + 1
            ineg = i - 1
            a = ipos < r and cake[ipos] == ['?']*c
            b = ineg >= 0 and cake[ineg] == ['?']*c
            while a and b:
                ipos += 1
                ineg -= 1
                a = ipos < r and cake[ipos] == ['?']*c
                b = ineg >= 0 and cake[ineg] == ['?']*c
            if ipos < r and not cake[ipos] == ['?']*c:
                cake[i] = cake[ipos]
            else:
                cake[i] = cake[ineg]

    for i in range(r):
        for j in range(c):
            if cake[i][j] != '?':
                jneg = j - 1
                jpos = j + 1
                while (jpos < c and cake[i][jpos] == '?') or (jneg >= 0 and cake[i][jneg] == '?'):
                    if jpos < c and cake[i][jpos] == '?':
                        cake[i][jpos] = cake[i][j]
                        jpos += 1
                    if jneg >= 0 and cake[i][jneg] == '?':
                        cake[i][jneg] = cake[i][j]
                        jneg -= 1
    for i in range(r):
        for j in range(c):
            if cake[i][j] != '?':
                char = cake[i][j]
                if (j == 0 or cake[i][j-1] != char) and (j == c-1 or cake[i][j+1] != char):
                    ipos = i + 1
                    ineg = i - 1
                    while (ipos < r and cake[ipos][j] == '?') or (ineg >= 0 and cake[ineg][j] == '?'):
                        if ipos < r and cake[ipos][j] == '?':
                            cake[ipos][j] = char
                            ipos += 1
                        if ineg >= 0 and cake[ineg][j] == '?':
                            cake[ineg][j] = char
                            ineg -= 1

    print("Case #", t0 + 1, ":", sep = '')
    for i in range(r):
        print(''.join([str(j) for j in cake[i]]))




