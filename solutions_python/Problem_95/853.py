import sys

mapping = { 'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q', ' ':' ' }

def readlines(f):
    num_lines = f.readline()
    for line in f:
        yield line[:-1]

def transform(lines):
    for line in lines:
        yield ''.join([mapping[ch] for ch in line])

def output(out_lines):
    for i, line in enumerate(out_lines):
        print 'Case #{i}: {o}'.format(i=i+1, o=line)

if __name__ == '__main__':
    in_lines = readlines(sys.stdin)
    out_lines = transform(in_lines)
    output(out_lines)
