getmaxmin = lambda x, s: x + 2*min(x + 2, 10) if s else x + 2*min(x + 1, 10)
getmin = lambda x, s: x + 2*max(x - 2, 0) if s else x + 2*max(x - 1, 0)

def gentriple(num, p):
    trip = (p,(p-1))
    num -= p
    num -= (p-1)
    trip += (num,)
    return trip

def validtrip(trip):
    return abs(max(trip) - min(trip)) < 2

def issup(trip):
    if len(trip) == 2:
        num = abs(trip[0] - trip[1])
        return num < 2
    else:
        return issup(trip[:2]) and issup(trip[1:]) and issup((trip[0], trip[2]))

def addtripq(trip,p):
    if type(trip) == int:
        return trip >= p
    else:
        rval = False
        for t in trip:
            rval = rval or addtripq(t, p)
        return rval

def dotest(s, p, googlers):
    suprange = range(getmin(p, True), 3*p + 1)
    normrange = range(getmin(p, False), 3*p + 1)
    outlier = list(set(suprange) - set(normrange))
    #print('suprange', suprange, 'normrange', normrange, 'outlier', outlier)
    num = 0
    min = getmin(p, False)
    for score in googlers:
       # print('score', score,'min', getmin(p, False))
        if score >= min:
       #     print('ding')
            num +=1
        else:
            if score in outlier and s > 0:
                num += 1
                s -= 1
    return num

print('min t',getmin(8, True))
print('min f',getmin(8, False))
print(issup((5,7,7)))

f = open('B-large.in')
fout = open('output','w')
outputcounter = [1]
def output(num):
    fout.write("Case #%s: %s\n" % (outputcounter[0], num))
    outputcounter[0] += 1

#f = open('test')
number = int(f.readline())

while number > 0:
    split = f.readline().split()
    print('split', split)
    split.reverse()
    N = int(split.pop())
    s = int(split.pop())
    p = int(split.pop())
    split = tuple(map(lambda a: int(a), split))
    print('type', type(p))
    output(dotest(s, p, split))
    number -= 1
