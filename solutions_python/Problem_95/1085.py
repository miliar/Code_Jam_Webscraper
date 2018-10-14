In [43]: translator
Out[43]:
{' ': ' ',
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
 'z': 'q'}

def solve(inp):
    inp_lines = inp.split("\n")[1:]
    output = []
    for line, i in zip(inp_lines, range(1, 31)):
        trans_line = "".join(translator[x] if x in line else x for x in line)
        output.append("Case #%d: %s" % (i, trans_line,))
    return "\n".join(output)
