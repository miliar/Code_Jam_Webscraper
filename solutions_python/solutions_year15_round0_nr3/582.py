import sys


table = {
    '1': {'1': '1', 'i':'i', 'j':'j', 'k':'k'},
    'i': {'1': 'i', 'i':'-1', 'j':'k', 'k':'-j'},
    'j': {'1': 'j', 'i':'-k', 'j':'-1', 'k':'i'},
    'k': {'1': 'k', 'i':'j', 'j':'-i', 'k':'-1'},
    '-': {'1': '-1', 'i':'-i', 'j':'-j', 'k':'-k',
          '-1': '1', '-i':'i', '-j':'j', '-k':'k'},
}


def mult(a, b):
    if a == '-':
        return table[a][b]

    if a.startswith('-'):
        return mult('-', mult(a[-1], b))
    return table[a][b]

def test_inputn(chars):
    from_start = chars[0]
    snds = set()
    thds = set()

    for i in range(1,len(chars)):
        cur = chars[i]
        new_2nds = set()
        new_3rds = set()
        if from_start == 'i':
            new_2nds.add(cur)
        if 'j' in snds:
            new_3rds.add(cur)

        from_start = mult(from_start, cur)
        snds = new_2nds.union([mult(x, cur) for x in snds])
        thds = new_3rds.union([mult(x, cur) for x in thds])

    if 'k' in thds:
        return "YES"
    else:
        return "NO"

def run_it(filename):
    fh = open(filename, "r")
    lines = fh.readlines()[1:]
    pairs = [lines[i:i+2] for i in range(0, len(lines), 2)]
    inputs = [p[1].strip()*int(p[0].split()[-1]) for p in pairs]

    #print inputs[:-1]
    outs = ["Case #{}: {}".format(i+1, test_inputn(inp)) for i, inp in
            enumerate(inputs)]

    with open("out.txt", "w+") as outfh:
        outfh.write("\n".join(outs))


run_it(sys.argv[1])
