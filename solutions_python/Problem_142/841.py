#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      udonko
#
# Created:     04/05/2014
# Copyright:   (c) udonko 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!/usr/bin/env python

#python 3.3.2


import sys
import collections
class Reslver:
    IMPOSSIBLE = "Fegla Won"
    def __init__(self, textarray):
        self.textarray = textarray
        self.resolve()
    def changedata(self, text):
        data = []
        lastch = '@'
        for ch in text:
            if ch != lastch:
                if lastch != '@':
                    data.append( (lastch, count)  )
                count = 1
                lastch = ch

            else:
                count+=1
        data.append( (lastch, count)  )

        return data

    def resolve(self):
        dif = 0
        others = []
        for index, text in enumerate(self.textarray):
            if index == 0:
                firstCnt = self.changedata(text)
            else:
                otherCnt = self.changedata(text)
                others.append(otherCnt)
                if len(firstCnt) != len(otherCnt):
                    self.result = Reslver.IMPOSSIBLE
                    return
                dif = 0
                for a,b in zip(firstCnt, otherCnt):
                    if a[0] != b[0]:
                        self.result =  Reslver.IMPOSSIBLE
                        return
        result = 0
        for index in range(len(firstCnt)):
            difmax = 0
            for other  in  others :
                difmax = max(difmax, abs(other[index][1]-firstCnt[index][1]))
            result += difmax
        self.result = result
        return
def main():
    filename = "A-small-attempt0 (2).in"
    with open(filename,"r") as inputfile:
        with open(filename+"out.txt","w") as outputfile:
            w = outputfile.write
            r = inputfile.readline;
            rt = r()
            t = int(rt)
            for i in range(t):
                rt = r()
                n= int(rt)
                textarray = []
                for j in range(n):
                    rt = r()
                    textarray.append(rt.strip())
                res = Reslver(textarray)
                outtext = "Case #{0}: {1}".format(i+1, res.result)

                print(outtext)
                w(outtext+"\n")




if __name__ == '__main__':
    main()
