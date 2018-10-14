__author__ = 'tibbar'

class quaternion():
    def __init__(self, char, negative=False):
        self.value = char
        self.negative = negative
    def __mul__(self, other):
        if self.negative and other.negative:
            negative = False
        elif self.negative or other.negative:
            negative = True
        else:
            negative = False
        if self == '1' and other == '1':
            answer = '1'
        if self == '1' and other == 'i':
            answer = 'i'
        if self == '1' and other == 'j':
            answer = 'j'
        if self == '1' and other == 'k':
            answer = 'k'
        if self == 'i' and other == '1':
            answer = 'i'
        if self == 'i' and other == 'i':
            answer = '1'
            if negative:
                negative = False
            else:
                negative = True
        if self == 'i' and other == 'j':
            answer = 'k'
        if self == 'i' and other == 'k':
            answer = 'j'
            if negative:
                negative = False
            else:
                negative = True
        if self == 'j' and other == '1':
            answer = 'j'
        if self == 'j' and other == 'i':
            answer = 'k'
            if negative:
                negative = False
            else:
                negative = True
        if self == 'j' and other == 'j':
            answer = '1'
            if negative:
                negative = False
            else:
                negative = True
        if self == 'j' and other == 'k':
            answer = 'i'
        if self == 'k' and other == '1':
            answer = 'k'
        if self == 'k' and other == 'i':
            answer = 'j'
        if self == 'k' and other == 'j':
            answer = 'i'
            if negative:
                negative = False
            else:
                negative = True
        if self == 'k' and other == 'k':
            answer = '1'
            if negative:
                negative = False
            else:
                negative = True
        x = quaternion(answer, negative)
        return x
    def __eq__(self, other):
        if isinstance(other, int):
            raise TypeError('type int')
        if isinstance(other, str):
            return self.value == other
        return self.value == other.value and self.negative == other.negative
    def __str__(self):
        if self.negative:
            return '-%s' %self.value
        else:
            return '%s' %self.value

def solve(str, multiple):
    #multiple = multiple%16
    one = quaternion('1')
    current = quaternion('1')
    [foundI, foundJ, foundK] = [False, False, False]
    i = 0
    while i < multiple:
        [current, foundI, foundJ, foundK] = solveIter(current, str, foundI, foundJ, foundK)
        i += 1
        #print(foundI, foundJ, foundK, '%s' %current)
    if foundI and foundJ and foundK and current == one:
        return 'YES'
    return 'NO'


def solveIter(current, str, foundI, foundJ, foundK):
    i = quaternion('i')
    j = quaternion('j')
    k = quaternion('k')
    posI = 0
    posJ = 0
    posK = 0
    for l in range(len(str)):
        c = str[l]
        q = quaternion(c)
        current *= q
        if not foundI and current == i:
            print('current: %s, Found i %s' %(current,str[0:l+1]))
            posI = l+1
            foundI = True
            current = quaternion('1')
        if not foundJ and foundI and current == j:
            print('current: %s, Found j %s' %(current,str[posI:l+1]))
            posJ = l+1
            foundJ = True
            current = quaternion('1')
        if not foundK and foundI and foundJ and current == k:
            print('current: %s, Found k %s' %(current,str[posJ:l+1]))
            posK = l
            foundK = True
            current = quaternion('1')
    return [current, foundI, foundJ, foundK]
f = open('C-small-attempt3.in')
out = []
first = f.readline()
T = int(first.strip())
#print(T)
for i in range(T):
    l = f.readline()
    [L, X] = l.split(' ')
    [L, X] = [int(L), int(X)]
    string = f.readline().strip()
    answer = solve(string, X)
    print(L, X, string, answer)
    out.append('Case #%d: %s\n' %(i+1,answer))
outF = open('out.txt', 'w')
outF.writelines(out)