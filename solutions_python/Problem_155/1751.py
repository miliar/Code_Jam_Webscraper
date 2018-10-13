from __future__ import print_function


import sys
def doit(audStr,minExtras):
    aud = list(audStr)
    aud = map(int, aud)
    for i in range(len(aud)+1):
        sumC = sumCritArr(aud,i)
        if((sumC>=minExtras)):
            return i
            minExtras = sumC

    # print cnt
    return minExtrasO


def outP(cNum, mNumf):
    # print("Case #" + str(cNum) + ": " +str( mNumf)+ "\n")
    # f = open('out','w')

    # print("Case #" + str(cNum) + ": " +str( mNumf), file=f)
    with open('out.txt','a') as oFile:
        oFile.write("Case #" + str(cNum) + ": " +str( mNumf)+"\n")

def breakblock(_t,s):
    # c = int(s[0])

    # aud = (s[1])
    zCnt = doit(s)
    outP(_t+1,zCnt)



def sumCritArr(arr, extras):
    sumC = extras
    for i in range(len(arr)):
        if(i<=sumC):
            sumC += (arr[i])
            continue    
        break
    return sumC


if __name__ == "__main__":

    file1 = "A-large.in"

    f = open(file1)
    t = int(f.readline())

    for _t in xrange(t):
        s = (f.readline().split())
        # c = int(s[0])

        zCnt = doit((s[1]),int(s[0]))
        outP(_t+1,zCnt)

    # sTest = "11111"
    # sTest1 = "09"
    # sTest2 = "110011"
    # sTest3 = "1"
    # breakblock(1,sTest)
    # breakblock(2,sTest1)
    # breakblock(3,sTest2)
    # breakblock(4,sTest3)

    # doit(sTest)
    # doit(sTest1)
    # doit(sTest2)
    # doit(sTest3)



    # f = sys.stdin

    # if len(sys.argv) >= 2:
    #     fn = sys.argv[1]
    #     if fn != '-':
    #         f = open(fn)
