# There's a stupid answer to the small case, we'll do that first

inputF = open('B-small-attempt0.in', 'r')
output = open('B-small-attempt0.out', 'w')

numCases = int(inputF.readline())

class colorCounter:
    def __init__(self, num, color):
        self.color = color
        self.num = num

    def __cmp__(self, other):
        return cmp(self.num, other.num)

    def __repr__(self):
        return str((self.color, self.num))

for i in range(numCases):
    line = inputF.readline().split()
    line = [int(j) for j in line]
    n = line[0]
    r = line[1]
    y = line[3]
    b = line[5]
    if r > n/2 or y > n/2 or b>n/2:    
        output.write('Case #' + str(i+1) + ': IMPOSSIBLE\n')
    else:
        s = '0'
        d = sorted([colorCounter(r, 'R'), colorCounter(b, 'B'), colorCounter(y, 'Y')])
        d[-1].num += 0.0001 # Perturb the first color so we don't end with it.
        for j in range(n):
            d = sorted(d)
            f = filter(lambda x: x.color != s[-1], d)
            s += f[-1].color
            f[-1].num -= 1
        print s[1:]
        output.write('Case #' + str(i+1) + ': ' + s[1:] + '\n')
            
inputF.close()
output.close()
