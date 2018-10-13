
class TestCase:

    def __init__(self, n, data, f):
        self.n = n
        self.data = data
        self.flip = f
        self.result = conv(self.data, self.flip)

    def p(self):
        return 'Case #{}: {}\n'.format(self.n,self.result)



def map(strarry):
    v = strarry.split(' ')
    r = []
    for u in v:
        r.append(int(u))
    return r

def conv(d, f):
    print (len(d))
    s = list(str(d))
    count = 0
    for i in range(len(d)-f+1):
        if s[i] == '-':
            count=count+1
            for j in range(f):
                s[i+j] = '+' if s[i+j] == '-' else '-'

    return count if complete("".join(s)) else 'IMPOSSIBLE'

def complete(d):
    for i in range(len(d)):
        if d[i] == '-':
            return False
    return True

# print '{} -> {}'.format(882,conv(882))
# print '{} -> {}'.format(110,conv(110))

inFile = 'A-large.in'
outFile = inFile.replace('.in', '.out')

inf = open(inFile, 'r')
outf = open(outFile, 'w')

data = inf.readlines()
noTests = int(data[0])
i=1
for d in data[1:]:
    row = d.split(' ')
    tc = TestCase(i, row[0], int(row[1]))
    outf.write(tc.p())
    print tc.p()
    i=i+1

outf.close()
inf.close()

