import pickle
import time

def isfair(x):
    return str(x) == str(x)[::-1]

def isqrt(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y
        
def issquare(x):
    xsqrt = isqrt(x)
    intsquare = xsqrt * xsqrt == x
    return isfair(x) and intsquare and isfair(xsqrt)
        
def palinsearch(a, b):
    count = 0
    for i in xrange(a, b+1):
        if issquare(i):
            count += 1
    return count
    
def genpalinlist(upper):
    list = []
    for i in xrange(upper+1):
        if isfair(i):
            list.append(i)
    return list
    
def genpalinlistfast(limit):
    result = []
    
    if limit < 9:
        end = limit + 1
    else:
        end = 10
    for i in range(end):
        result.append(i)
        
    cont = True
    counter = 1
    while cont:
        rev = str(counter)[::-1]
        cont = False
        digits = list('0123456789')
        digits.append('')
        for d in digits:
            n = int(str(counter) + d + rev)
            if n <= limit:
                cont = True
                result.append(n)
        counter += 1
        
    return result
    
def palinsearchfast(a, b, palinlist):
    count = 0
    for palin in palinlist:
        palinsquare = palin**2
        if palinsquare >= a and palinsquare <= b:
            count += 1
    return count
 
def readfile(input, output, palinlist):
    counter = 0
    answer = open(output, 'w')
    for line in open(input, 'r').readlines()[1:]:
        counter += 1
        cool = line.replace('\n', '').split(' ')
        nums = []
        for item in cool:
            nums.append(int(item))
            
        answer.write('Case #' + str(counter) + ': ' + str(palinsearch(nums[0], nums[1])) + '\n')
        
palinlist = genpalinlistfast(10**8)
readfile('C-small-attempt0.in', 'testanswer.txt', palinlist)
        
#start = time.time()
#palinlist = genpalinlistfast(10**8)
#print len(palinlist)
#print time.time() - start
#print palinsearchfast(1, 10**14, palinlist)
#print time.time() - start