file = open('A-large.in', 'r') # r for read
# file = open('a.in', 'r') # r for read
out = open('a.out', 'w') # w for write
#
n = int(file.readline().strip()) 
for n in range(n):
    out.write('Case #{}:\n'.format(1+n))

    l = file.readline().strip().split(' ')
    R = int(l[0])
    C = int(l[1])

    cake = []
    for r in range(R):
        cake.append(list(file.readline().strip()))

    revisit = []
    for r in range(R):
        if cake[r] == ['?']*C:
            revisit += [r]
            # print('adf')
            # print(n+1,revisit)
            continue


        letter = '?'
        for c in range(C):
            if cake[r][c] == '?':
                cake[r][c] = letter
            else:
                letter = cake[r][c]
        # print(cake)
        if cake[r][0] == '?':
            for c in range(C-1, -1, -1):
                if cake[r][c] == '?':
                    cake[r][c] = letter
                else:
                    letter = cake[r][c]

    revisit = sorted(revisit)
    # print(n+1, revisit)
    # print(cake)
    cp = 0
    while cp in revisit:
        cp += 1
    # print(cp)

    cake[0] = cake[cp][:]

    for r in revisit:
        if r == 0:
            continue
        cake[r] = cake[r-1][:]

    for r in cake:
        out.write(''.join(r) + '\n')
    # print(cake)
    # print()
    # print()
#
file.close()
out.close()