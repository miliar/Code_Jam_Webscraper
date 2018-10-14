import sys

mapping = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's',
           'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u',
           'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r',
           's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p',
           'y': 'a', 'x': 'm', 'z': 'q'}

inputiter = iter(sys.stdin)
line = inputiter.next()
input_count = int(line)

for case_number, line in enumerate(inputiter):
    translated_line = ''.join((mapping[x] for x in line.strip()))
    print 'Case #{}: {}'.format(case_number + 1, translated_line)