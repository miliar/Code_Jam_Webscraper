import sys

filename = sys.argv[1]
outputfile = "cookieresult"

def cookiecal(c, f, x, items):
    ret = 0
    product = 2
    for i in range(items):
        ret += c / product
        product += f
    ret += x / product
    return ret

fi = open(filename, 'r')
fo = open(outputfile, 'w')

caseNum = int(fi.readline())
for i in range(caseNum):
    [c, f, x] = [float(item) for item in fi.readline().split(' ')]
    case = str(i + 1)
    upper = f * x - 2 * c
    if upper > 0:
        n = int(upper / f / c)
    else:
        n = 0
    result = cookiecal(c, f, x, n)
    fo.write("Case #{0}: {1:.7f}\r\n".format(i+1, result))

    
