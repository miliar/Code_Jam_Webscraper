from sys import stdin

#efficient char encoding for negative numbers
mappingneg = {}
mappingneg['1'] = 'a'
mappingneg['i'] = 'b'
mappingneg['j'] = 'c'
mappingneg['k'] = 'd'
mappingneg['a'] = '1'
mappingneg['b'] = 'i'
mappingneg['c'] = 'j'
mappingneg['d'] = 'k'

mapping = {}
mapping[('1', '1')] = '1'
mapping[('1', 'i')] = 'i'
mapping[('1', 'j')] = 'j'
mapping[('1', 'k')] = 'k'
mapping[('i', '1')] = 'i'
mapping[('i', 'i')] = 'a'
mapping[('i', 'j')] = 'k'
mapping[('i', 'k')] = 'c'
mapping[('j', '1')] = 'j'
mapping[('j', 'i')] = 'd'
mapping[('j', 'j')] = 'a'
mapping[('j', 'k')] = 'i'
mapping[('k', '1')] = 'k'
mapping[('k', 'i')] = 'j'
mapping[('k', 'j')] = 'b'
mapping[('k', 'k')] = 'a'

updatemapping = {}
for k, v in mapping.viewitems():
    updatemapping[(mappingneg[k[0]], mappingneg[k[1]])] = v
    updatemapping[(mappingneg[k[0]], k[1])] = mappingneg[v]
    updatemapping[(k[0], mappingneg[k[1]])] = mappingneg[v]
mapping.update(updatemapping)


def readline():
    return stdin.readline().strip()


def solve(inp):
    lenp = len(inp)
    val = '1'
    for i in xrange(0, lenp):
        val = mapping[(val, inp[i])]
    if val != 'a':
        return False
    val = '1'
    ioptions = []
    for i in xrange(0, lenp):
        val = mapping[(val, inp[i])]
        if val == 'i':
            ioptions.append(i + 1)
    koptions = []
    val = '1'
    for i in xrange(lenp - 1, -1, -1):
        val = mapping[(inp[i], val)]
        if val == 'k':
            koptions.append(i - 1)
    for i in ioptions:
        for j in koptions:
            if i > j:
                continue
            val = '1'
            for p in xrange(i, j + 1):
                val = mapping[(val, inp[p])]
            if val == 'j':
                return True
    return False


if __name__ == "__main__":
    numofcases = int(readline())
    for i in range(numofcases):
        l, x = map(int, readline().split(' '))
        #This is an optimization because a whole repetetive section could be maximum 4 times
        #if x > 15:
            #x = 15
        inp = readline() * x
        print 'Case #%d: %s' % (i + 1, 'YES' if solve(inp) else 'NO')
