from sys import argv
from re import sub, findall

def read(inputfile):
    g = inputfile.readline()
    return sub('\n','',g)

inp = open('input.txt')
out = open('output.txt')

inT = int(read(inp))
mapping = {}

for t in range(inT):
    line = read(inp)
    expected = read(out)

    # create mapping
    for i in range(len(line)):
        expected = sub('Case #[\d]: ','',expected)
        mapping[line[i]] = expected[i]
    # q and z custom mapping
    mapping['q'] = 'z'
    mapping['z'] = 'q'

# translate
f = open(argv[1])
T = int(read(f))

for t in range(T):
    line = read(f)
    translated = []
    for c in line:
        translated.append(mapping[c])
    translated = ''.join(translated)
    print("Case #%s:" % (t+1),translated)
