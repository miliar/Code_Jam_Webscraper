def out_of_bounds(cakes, flipper, i):
    if (len(cakes) - i) < flipper:
        return True

def flip_cake(i, cakes, flipper):
    for x in range(flipper):
        if cakes[i + x] == '-':
            cakes[i + x] = '+'
        else:
            cakes[i + x] = '-'
    return cakes

def flip_left_to_right(cakes, flipper):
    print()
    print(cakes)
    print(flipper)
    print()
    i = 0
    flips = 0
    while True:
        if out_of_bounds(cakes, flipper, i):
            if '-' in cakes:
                return 'IMPOSSIBLE'
            return flips
        else:
            cake = cakes[i]
            if cake == '-':
                cakes = flip_cake(i, cakes, flipper)
                flips += 1
        i += 1


print(flip_left_to_right(['-', '-', '-', '+', '-', '+', '+', '-'], 4))


with open('text.txt') as f:
    text = [x.strip() for x in f.readlines()][1:]
    text = [x.split() for x in text]
    text = [{'cakes':list(x), 'flipper':int(y)} for x, y in text]
    print(text)

outputs = []
for i, val in enumerate(text):
    output = flip_left_to_right(val['cakes'], val['flipper'])
    outputs += ["Case #{}: ".format(i+1) + str(output)]

print(outputs)

with open('output.txt', 'w+') as f:
    f.write('\n'.join([str(x) for x in outputs]))
