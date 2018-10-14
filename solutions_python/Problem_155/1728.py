__author__ = 'Tony'

def WTF(inty):
    f = open('big.out','a')
    f.write(inty+'\n') # python will convert \n to os.linesep
    f.close()

with open("A-large.in") as f:
    content = f.readlines()
numOfTests = int(content[0])
for testNum in xrange(1,numOfTests+1):
    stringy = content[testNum].split(" ")
    sMax = int(stringy[0])
    x = list(stringy[1])
    helping = 0
    standing = int(x[0])
    for y in xrange(1,sMax+1):
        if ((standing >= y) & (int(x[y])>0)):
            standing = standing +int(x[y])
            continue
        if ((standing < y) & (int(x[y])>0)):
            helping = helping+(y-standing)
            standing = y+int(x[y])
    WTF("Case #"+str(testNum)+": "+str(helping))

