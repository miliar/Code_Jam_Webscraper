import sys
filein, fileout = sys.argv[1:3]

def solve(line):
    splits = list(line.split())
    c = int(splits.pop(0))
    cs = {x[:2]: x[2] for x in [splits.pop(0) for i in range(c)]}
    d = int(splits.pop(0))
    ds = [splits.pop(0) for i in range(d)]
    n, invokes = splits
    n = int(n)
    elements = []
    for e in invokes:
        elements.append(e)
        last = ''.join(elements[-2:])
        while last in cs or last[::-1] in cs:
            elements.pop()
            elements.pop()
            if last in cs:
                elements.append(cs[last])
            elif last[::-1] in cs:
                elements.append(cs[last[::-1]])
            else:
                raise KeyError("last not in cs...?")
            last = ''.join(elements[-2:])
        for a,b in ds:
            if a in elements and b in elements:
                elements = []
    return '['+', '.join(elements)+']'

if __name__ == '__main__':
    with open(filein, 'rU') as f1, open(fileout, 'w') as f2:
        T = int(f1.readline())
        for case in range(T):
            f2.write("Case #{}: {}\n".format(case+1, solve(f1.readline().strip())))
