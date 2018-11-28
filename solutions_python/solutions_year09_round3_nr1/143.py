
def read_file(filename):
    f = open(filename)
    contents = f.read().splitlines()
    return contents

contents = read_file('A-large.in')
T = int(contents.pop(0))

def decipher_case(case):
    min_base = max(2, len(set(case)))
    counter = 0
    table = {}
    first = case[0]
    for i in range(len(case)):
        if case[i] != first:
            table[case[i]] = 0
            break
    for char in case:
        if not table.has_key(char):
            table[char] = counter + 1
            counter += 1
    sum = 0
    for i, char in enumerate(reversed(case)):
        sum += table[char] * (min_base ** i)
    return sum

for i, case in enumerate(contents):
    print 'Case #%d: %d' % (i+1, decipher_case(case))
