def flipsingle(cake):
    return '+' if cake == '-' else '-'


def flip(cakes, index, size):
    #print('gonna flip', cakes, index, size)
    for i in range(index, index+size):
        cakes[i] = flipsingle(cakes[i])


numcases = int(input())

for i in range(numcases):
    cakes, size = input().split(' ')

    cakes = list(cakes)
    size = int(size)

    numflips = 0

    for j, cake in enumerate(cakes):
        if cake == '-':
            try:
                flip(cakes, j, size)
                numflips += 1
            except IndexError:
                numflips = -1
                break

    if numflips == -1:
        print('Case #' + str(i+1) + ': ', 'IMPOSSIBLE')
    else:
        print('Case #' + str(i+1) + ': ', numflips)
