t = int(input())

for i in range(1, t + 1):
    R, C = [int(s) for s in input().split(' ')]
    cake = [None] * R

    for r in range(R):
        L = list(input())
        cake[r] = L

    for r in range(R):
        for c in range(C):
            current = cake[r][c]
            running = True
            if current == '?':
                for l in range(c, C):
                    if cake[r][l] != '?':
                        cake[r][c] = cake[r][l]
                        break

    for r in range(R):
        for c in range(C):
            current = cake[r][c]
            running = True
            if current == '?':
                for l in range(c, -1, -1):
                    if cake[r][l] != '?':
                        cake[r][c] = cake[r][l]
                        break

    for r in range(R):
        for c in range(C):
            current = cake[r][c]
            running = True
            if current == '?':
                for l in range(r, R):
                    if cake[l][c] != '?':
                        cake[r][c] = cake[l][c]
                        break

    for r in range(R):
        for c in range(C):
            current = cake[r][c]
            running = True
            if current == '?':
                for l in range(r, -1, -1):
                    if cake[l][c] != '?':
                        cake[r][c] = cake[l][c]
                        break


    print('Case #{}:'.format(i))
    for c in cake:
        print(''.join(c))
