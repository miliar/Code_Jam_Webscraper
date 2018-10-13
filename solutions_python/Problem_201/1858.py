
class TestCase:

    def __init__(self, num, n, k):
        self.num = num
        self.result = conv(n,k)
        self.result.sort(reverse=True)

    def p(self):
        return 'Case #{}: {} {}\n'.format(self.num,self.result[0],self.result[1])



def map(strarry):
    v = strarry.split(' ')
    r = []
    for u in v:
        r.append(int(u))
    return r

def conv(n,k):
    space = []
    space.append(n)
    #print space
    for i in range(k):
        #print space
        max = space.pop(0)
        #print max

        result = []
        result.append(max / 2)
        if max % 2 == 0:
            result.append((max/2)-1)
        else:
            result.append(max/2)
        space = space + result

        space.sort(reverse=True)

    result.sort(reverse=True)
   # print space
    return result

#print '{} -> {}'.format("999 3",conv(999,3))
# print '{} -> {}'.format(110,conv(110))

inFile = 'C-small-1-attempt2.in'
#inFile = 'max.in'
outFile = inFile.replace('.in', '.out')

inf = open(inFile, 'r')
outf = open(outFile, 'w')

data = inf.readlines()
noTests = int(data[0])
i=1
for d in data[1:]:
    row = d.split(' ')
    tc = TestCase(i, int(row[0]), int(row[1]))
    outf.write(tc.p())
    print tc.p()
    i=i+1

outf.close()
inf.close()

