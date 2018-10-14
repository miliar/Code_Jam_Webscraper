import math
import operator

def lrange(num1, num2 = None, step = 1):
    op = operator.__lt__

    if num2 is None:
        num1, num2 = 0, num1
    if num2 < num1:
        if step > 0:
            num1 = num2
        op = operator.__gt__
    elif step < 0:
        num1 = num2

    while op(num1, num2):
        yield num1
        num1 += step

def getminmax(filename):
    with open(filename) as f:
        T = int(f.readline())
        omin = 0
        omax = 0
        for i in range(0, T):
            count = 0
            line = f.readline().strip().split(" ")
            minN = int(line[0])
            maxN = int(line[1])
            if minN < omin:
                omin = minN
            if maxN > omax:
                omax = maxN
        return (omin, omax)

def createrange(omin, omax):
    arr = {}
    count = 1
    i = 0
    count = omin
    oto = int(math.sqrt(omax))
    while count <= oto:
        if(str(count) == str(count)[::-1]):
            sqrcount = count*count
            if(str(sqrcount) == str(sqrcount)[::-1]):
                arr[i] = sqrcount
                i = i+1
        count = count + 1
    return arr

def main():
    filename = 'C-large-1.in'
    omin, omax = getminmax(filename)
    array = createrange(omin, omax)
    with open(filename) as f:
    #with open('test.in') as f:
        T = int(f.readline())
        for i in range(0, T):
            count = 0
            line = f.readline().strip().split(" ")
            minN = int(line[0])
            maxN = int(line[1])
            for num in array:
                if array[num] >= minN and array[num] <= maxN:
                    count = count+1

##            for num in lrange(minN, maxN+1):
##                strnum = str(num)
##                if(strnum == strnum[::-1]):
##                    temp = int(math.floor(math.sqrt(num)))
##                    if(temp*temp == num):
##                        if(str(temp) == str(temp)[::-1]):
##                            count = count+1
            print "Case #"+str(i+1)+": "+str(count)



if __name__ == '__main__':
    main()
