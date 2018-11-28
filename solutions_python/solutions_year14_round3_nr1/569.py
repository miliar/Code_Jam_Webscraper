__author__ = 'Indika'
#from __future__ import division

file_path = 'data_files/2014/'
filename = 'A-large.in'


def stringToIntList(line):
    intList = line.split('/')
    intList = [int(x) for x in intList]
    return intList

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

class frac:
    top = None
    bot = None

    def __init__(self, _top,_bot):
        self.top = _top
        self.bot = _bot

    def __str__(self):
        return str(self.top)+'/'+str(self.bot)

    def simplify(self):
        factor = gcd(self.top, self.bot)
        self.top = self.top/factor
        self.bot = self.bot/factor

def isValid(fraction, powList):
    for i in powList:
        if fraction.bot == i:
            return True
    return False

f = open(file_path + filename, 'r')
out_file = open(file_path + filename + '.out', 'w')


# create powers of 2 array
pow2 = [1]
num = 1
for i in range(1,41):
    num *= 2
    pow2.append(num)

#print(pow2)

#read from file
s = f.readline()
numTestCases = int(s)
for i in range(0,numTestCases):
    prefix = 'Case #' + str(i+1) + ': '
    temp = stringToIntList(f.readline())
    part = frac(temp[0],temp[1])
    part.simplify()
    if isValid(part, pow2):
        #do stuff here
        val = float(part.top)/part.bot
        for x in range(1,41):
            s = 1.0/pow2[x]
            if val-s >= 0:
                out_file.write(prefix + str(x)+'\n')
                print(x)
                break
    else:
        out_file.write(prefix + 'impossible'+'\n')
        print('impossible')

