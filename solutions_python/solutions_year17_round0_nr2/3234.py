t = int(raw_input())
for c in xrange(t):
    number = [int(x) for x in raw_input()]
    for i in xrange(len(number) - 1):
        if number[i] > number[i + 1]:
            number[i] -= 1
            for j in xrange(i + 1, len(number)):
                number[j] = 9

            for j in xrange(i, 0, -1):
                if number[j] < number[j - 1]:
                    number[j] = 9
                    number[j - 1] -= 1

    to_cut = 0
    i = 0
    while i < len(number) and number[i] == 0:
        i += 1
        to_cut += 1

    number = number[to_cut:]
    out = 'Case #%s: ' % (c + 1)
    if number:
        out += ''.join([str(x) for x in number])
    else:
        out += '0'

    print(out)