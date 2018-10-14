from __future__ import print_function

def cyclenum(num):
    #print('num %s' % (num))
    if not len(num) == 1:
        num.insert(0, num.pop())

pairs = list()

def testnum(num, end):
    #print('start num %s' %(num))
    #print('start %s end %s' % (start, end))
    start = list(num)
    startval = getval(start)
    cycles = len(num)
    dig = len(num)
    #pairs = list()
    suc = 0
    while cycles > 0:
        cyclenum(num)
        numval = getval(num)
        #print('    cycles %s' % cycles)
        #print('    num%s'% num)
        #print('    start %s' % start)
        #print('    pairs %s tuple %s cycles %s' %(pairs, (startval, numval), cycles))
        #print('    val %s' % ( getval(num) ) )
        #print('    dig %s len %s' % ( dig, len(num)))
        #print('    first %s second %s third %s' % ( (dig == len(num)), (numval > start), (numval < end)))
        if dig == len(num) and  startval < numval and numval <= end and (startval, numval) not in pairs:
            suc += 1  
            tup = (startval,)
            tup += (numval,)
            pairs.insert(0,(getval(start),getval(num)))  
            #print('suc %s start %s end %s' % (tup,startval, end), end='')
        cycles -= 1
    return suc

def getval(num):
    #print('getval %s' % num)
    if len(num) == 1:
        return num[0]
    return reduce(lambda a,b: a*10 + b, num)

def makenum(number):
    rval = []
    while number > 0:
        rval.insert(0, number % 10)
        number = number / 10
    return rval

t = makenum(1234)
print('makenum', t)
print('getval', getval(t))
cyclenum(t)
print('cycle', t)

f = open('C-small-attempt2.in')
fout = open('output','w')
outputcounter = [1]
def output(num):
    print('num', num)
    fout.write("Case #%s: %s\n" % (outputcounter[0], num))
    outputcounter[0] += 1

#f = open('test')
number = int(f.readline())
print('number', number)

from sets import Set

while number > 0:
    pairs = list()
    stuff = f.readline().strip().split()
    print('stuff', stuff)
    a = int(stuff[0])
    b = int(stuff[1])
    tot = 0
    while a < b:
        #print('a', a, 'b', b)
        tot += testnum(makenum(a), b)
        a += 1
    output(tot)
    number -= 1
