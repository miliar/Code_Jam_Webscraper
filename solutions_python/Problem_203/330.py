def convert(row):
    symb = '1'
    first = '?'
    line_out = []
    for s in row:
        if s != '?':
            symb = s
            if first == '?':
                first = symb
        line_out.append(symb)
    return ''.join(line_out).replace('1', first)

def expand(rows):
    slice = None
    first = None
    cake_out_one = []
    for r in rows:
        if r[0] != '?':
            slice = r
            if first == None:
                first = slice
        if slice != None:
            cake_out_one.append(slice)
        else:
            cake_out_one.append(r)
    cake_out = []
    for r in cake_out_one:
        if r[0] == '?':
            cake_out.append(first)
        else:
            cake_out.append(r)
    return cake_out


with open('input.txt') as inp:
    with open('output.txt', 'w') as outp:
        ncases = int(inp.readline().strip())
        for nc in range(0, ncases):
            R, C = inp.readline().strip().split(' ')
            rows = []
            for i in range(0, int(R)):
                rows.append(convert(inp.readline().strip()))
            outp.write("Case #{}:\n".format(nc + 1))
            for r in expand(rows):
                outp.write("{}\n".format(convert(r)))