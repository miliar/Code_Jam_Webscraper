import string, sys

table = string.maketrans('ynficwlbkuomxsevzpdrjgthaq', ''.join([chr(i) for i in range(97, 123)]))

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    x = int(f.readline())
    out = open('result.out', 'w')
    i = 1
    while x:
        out.write('Case #%d: %s' % (i, f.readline().translate(table)))
        x -= 1
        i += 1