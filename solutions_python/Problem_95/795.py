import sys

langMap = {
    'a': 'y',
    'c': 'e',
    'b': 'h',
    'e': 'o',
    'd': 's',
    'g': 'v',
    'f': 'c',
    'i': 'd',
    'h': 'x',
    'k': 'i',
    'j': 'u',
    'm': 'l',
    'l': 'g',
    'o': 'k',
    'n': 'b',
    'p': 'r',
    's': 'n',
    'r': 't',
    'u': 'j',
    't': 'w',
    'w': 'f',
    'v': 'p',
    'y': 'a',
    'x': 'm',
    'z': 'q',
    'q': 'z',
    ' ': ' ',
    '\n': '\n'
}


def main():
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    with open(inputFile) as infile, open(outputFile,'w') as output:
        infile.readline()
        lineNum = 0
        for line in infile:
            lineNum += 1
            runTestCase(lineNum, line, output)


def runTestCase(lineNum, line, outputFile):
    output = []
    for char in line:
        output.append(langMap[char])
    outputFile.write('Case #{0}: {1}'.format(lineNum, ''.join(output)))


if __name__ == '__main__':
    main()
