mapping ={
    ' ': ' ',
    'a': 'y',
    'b': 'h',
    'c': 'e',
    'd': 's',
    'e': 'o',
    'f': 'c',
    'g': 'v',
    'h': 'x',
    'i': 'd',
    'j': 'u',
    'k': 'i',
    'l': 'g',
    'm': 'l',
    'n': 'b',
    'o': 'k',
    'p': 'r',
    'q': 'z',
    'r': 't',
    's': 'n',
    't': 'w',
    'u': 'j',
    'v': 'p',
    'w': 'f',
    'x': 'm',
    'y': 'a',
    'z': 'q'
}
def translate(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ret = []
    for char in string:
        ret.append(mapping[char])
    return "".join(ret)

if __name__ == "__main__":
    import sys
    inputs = []
    with file(sys.argv[1], 'r') as f:
        inputs = [ line.rstrip('\n') for line in f.readlines()[1:]]
    with file(sys.argv[2], 'w') as f:
        for i,input in enumerate(inputs):
            f.write('Case #%d: %s\n' % (
                i + 1,
                translate(input)
            ))
