import itertools
import numpy

def function2(fi,fo):
    f = open(fi)
    f2 = open(fo,"w")
    cases = int(f.readline())
    
    for nc,case in enumerate(range(cases)):
        ncan = int(f.readline()[0:-1].split(" ")[0])
        # ----------------------------------
        # Code here
        # ---------------------------------
        can =  f.readline()[0:-1].split(" ")
        can = map(lambda x: int(x),can)
        sumcan = sum(can)
        justo = sumcan/float(2)
        maxg = ncan/2
        diff = -1
        npos = 0
        res = "NO"
        opt = "NO"
        if len(set(can)) == 1:
            res = can[0]
        else:
            for i in range(1,maxg+1):
                for group in itertools.combinations(can,i):
                    group2 = list(set(can)-set(group))
                    fsum1 = sumlist(group)
                    fsum2 = sumlist(group2)
                    sum1 = sum(group)
                    sum2 = sum(group2)
                    if fsum1 == fsum2:
                        npos += 1
                        if max(sum2,sum1) > diff:
                            diff = max(sum2,sum1)
                            opt = (group,group2)
                            res = diff
        print "Case #" + str(nc+1) + ": "  + str(res)
        text = "Case #" + str(nc+1) + ": "  + str(res)
        f2.write(text + "\n")

def equisize(number,number2):
    maxl = len(max([number,number2],key=lambda x: len(x)))
    if len(number) != maxl:
        number = list(number)
        zs = list(numpy.zeros(maxl - len(number)))
        zs = map(lambda x: str(int(x)),zs)
        number = zs + number
        number = "".join(number)

    if len(number2) != maxl:
        number2 = list(number2)
        zs = list(numpy.zeros(maxl - len(number2)))
        zs = map(lambda x: str(int(x)),zs)
        number2 = zs + number2
        number2 = "".join(number2)
    return(number,number2)
    

def sumlist(numbers):
    bina = list(bin(numbers[0])[2:])
    bina.reverse()
    binaries = [bina]
    maxl = len(binaries[0])
    for i in numbers[1:]:
        bina = list(bin(i)[2:])
        bina.reverse()
        binaries += [bina]
        if len(binaries[-1])> maxl:
            maxl = len(binaries[-1])
    for ni,i in enumerate(binaries):
        extra = list(numpy.zeros(maxl-len(i)))
        extra = map(lambda x: int(x),extra)
        binaries[ni] = i + extra
    result = list(numpy.zeros(maxl))
    result = map(lambda x: int(x),result)
    binaries = numpy.matrix(binaries).transpose().tolist()
    for ni in range(maxl):
        count = binaries[ni].count('1')
        if count%2 !=0:
            result[ni] = 1
    result.reverse()
    result = map(lambda x: str(x),result)
    result = "".join(result)
    return int(result,2)

#function2("test.in","test.txt")
function2("short.in","short.txt")
#function2("long.in","long.txt")

