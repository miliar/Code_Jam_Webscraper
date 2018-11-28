file = "C-small-attempt0"

with open(file + ".in", "r") as input:
    lines = input.readlines()

if len(lines) - 1 != int(lines[0]):
    raise Exception("Number of test cases does not match header.")

cases = []
for line in lines[1:]:
    a, b = line.strip().split(' ')
    if len(a) != len(b):
        raise Exception("Numbers are not the same number of digits (%s, %s)" % (a, b))

    a = int(a)
    b = int(b)

    pairs = []

    n = a
    while n <= b:
        chars = str(n)
        if len(chars) > 1:
            for i in range(1, len(chars)):
                m = int(chars[i:] + chars[:i])
                pair = (n, m)
                #print i, pair, chars[i:], chars[:i]
                if pair[0] != pair[1] and m >= a and m <= b and pair not in pairs and (pair[1], pair[0]) not in pairs:
                    pairs.append(pair)
        n += 1
    cases.append(len(pairs))

with open(file + '.out', 'w') as output:
    for i, pairs in enumerate(cases):
        output.write('Case #%d: %d\n' % (i+1, pairs))
