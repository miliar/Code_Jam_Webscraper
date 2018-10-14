import sys

def make_mapping(mapping, in_s, out):
    for a,b  in zip(in_s,out):
        if not a == ' ':
            mapping[a] = b

def translate(in_s):
    m = {'a': 'y',
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
 'z': 'q',
 ' ': ' '}
    out = ''
    for i in in_s:
        out += m[i]
    return out

out_f = open(sys.argv[2],'w')
with open(sys.argv[1]) as in_f:
    T = int(in_f.readline())
    for t in range(T):
        text = in_f.readline().strip()
        print >> out_f, "Case #%d: %s" % (t+1,translate(text))



