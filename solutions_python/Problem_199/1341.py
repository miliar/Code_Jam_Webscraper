

def flip(flipper_size, pancakes):
    pancakes = list(pancakes)
    flipper_size = int(flipper_size)
    flips = 0
    #print(flipper_size)
    for i in range(0, len(pancakes) - flipper_size + 1):
        if pancakes[i] == '-':
            for c in range(i, i + flipper_size):
                if pancakes[c] == '-':
                    pancakes[c] = '+'
                elif pancakes[c] == '+':
                    pancakes[c] = '-'
            flips += 1
        #print(pancakes)

    for i in range(len(pancakes) - flipper_size, len(pancakes)):
        if pancakes[i] == '-':
            return 'IMPOSSIBLE'
    return flips


if __name__ == '__main__':
    with file('A-large.in') as f:
        _data = f.readline()
        _data = f.readline()
        i = 1
        while _data:
            pancakes, flipper_size = _data.split(' ')
            print("Case #{x}: {y}".format(x=i, y=flip(flipper_size, pancakes)))
            _data = f.readline()
            i += 1
