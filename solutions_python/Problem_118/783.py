import math

def isPal(num):
    nStr = str(num)
    
    for i in xrange(len(nStr) / 2):
        if nStr[i] != nStr[len(nStr)-1-i]:
            return False

    return True

def getPals(length):
    pals = []
    nums = ''
    r = length/2
    even = length % 2
    r += even

    if(length == 1):
        return range(1, 10);
    
    for i in xrange(r):
        nums += '1'

    maxVal = 10 ** r

    #print length, r, maxVal, even
    nums = int(nums)
    #print nums
    while nums < maxVal:
        pals.append(int(str(nums) + str(nums)[::-1][even:]))
        nums += 1

    return pals

def numOfPals(start, end):
    nums = 0
    st = int(math.sqrt(start)+0.2)
    en = int(math.sqrt(end)+0.2)
    if st**2 < start:
        st += 1
    if en**2 > end:
        en -= 1

    for i in xrange(len(str(st)), len(str(en))+1):
        pals = getPals(i)
        for pal in pals:
            if pal >= st and pal <= en:
                if isPal(pal**2):
                    nums +=1
            

    return nums


f = open('1-small-practice.in.txt', 'r')
fw = open('1-small-out.txt', 'w')

for i in xrange(int(f.readline())):
    start, end = [int(j) for j in f.readline().split()]


    fw.write('Case #' + str(i+1) + ': ' + str(numOfPals(start, end)) + '\n')

fw.close()
f.close()
