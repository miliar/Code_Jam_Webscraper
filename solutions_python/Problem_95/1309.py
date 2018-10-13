__author__ = 'jm679'


mapping = {
    'y': 'a',
    'n': 'b',
    'f': 'c',
    'i': 'd',
    'c': 'e',
    'w': 'f',
    'l': 'g',
    'b': 'h',
    'k': 'i',
    'u': 'j',
    'o': 'k',
    'm': 'l',
    'x': 'm',
    's': 'n',
    'e': 'o',
    'v': 'p',
    'z': 'q',
    'p': 'r',
    'd': 's',
    'r': 't',
    'j': 'u',
    'g': 'v',
    't': 'w',
    'h': 'x',
    'a': 'y',
    'q': 'z',
    ' ': ' ',
}

def translate(fh_in, fh_out):
    cases = int(fh_in.readline())

    for i in range(1, cases+1):
        fh_out.write("Case #%i: %s\n"%(i, "".join(mapping[w] for w in fh_in.readline()[:-1])))



if __name__ == '__main__':

    # Validate command line args
    import sys
    import os

    args = sys.argv
    if len(args) != 2:
        raise Exception("Single filename argument required")

    input_filename = args[1]
    output_filename = "%s.out"%(os.path.splitext(input_filename)[0])
    fh_in = open(input_filename)
    fh_out = open(output_filename, 'w')

    translate(fh_in, fh_out)