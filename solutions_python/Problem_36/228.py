import sys

needle = 'welcome to code jam'

sample_paragraph = '''So you've registered. We sent you a welcoming email, to welcome you to code jam. But it's possible that you still don't feel welcomed to code jam. That's why we decided to name a problem "welcome to code jam." After solving this problem, we hope that you'll feel very welcome. Very welcome, that is, to code jam.'''

'elcomew elcome to code jam'

t = 'wweellccoommee to code qps jam'
#2  2 2 2 2 2 2 (            1)

def generate_substrs(paragraph):
    total = len(paragraph)
    needle_len = len(needle)
    for x in xrange(total-needle_len, -1, -1):
        yield paragraph[x:]

def search_recurse(n, p):
    if not n: return 1
    if not p: return 0
    myn = n[0]
    restn = n[1:]
    ret = 0
    for i in xrange(len(p)):
        if p[i] == myn:
            ret += search_recurse(restn, p[i+1:])
    return ret


def put_output(out, number, count):
    out.write('Case #%d: %04d\n' % (number, count % 10000))

def run(infile, outfile):
    input = open(infile, 'r')
    lines = input.readlines()
    input.close()
    outfile = open(outfile, 'w')
    first = lines.pop(0).strip()
    num = int(first)
    for i in xrange(num):
        p = lines.pop(0).strip()
        put_output(outfile, i+1, search_recurse(needle, p))
        outfile.flush()
    outfile.close()
if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2])
