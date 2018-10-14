import sys
import math
import re
import io
import queue
import numpy as np

inputFile = "D:\\Downloads\\" + sys.argv[1]
outFile = "D:\\Downloads\\" + sys.argv[2]


class A:

    def __init__(self,file):
        line = file.readline().strip().split(" ")
        groupsNum = int(line[0])
        chocolateInPackage = int(line[1])
        groupsLine = file.readline().strip().split(" ")
        groups = []
        ans = 0
        for g in groupsLine:
            val = int(g) % chocolateInPackage
            if (val==0):
                ans+=1
            else:
                groups.append(val)
        start=0
        while(start<len(groups)):
            i=-1
            val=-1
            for i in range(start+1,len(groups)):
                val=(groups[start]+groups[i])%chocolateInPackage
                if(val==0):
                    break
            if (val==0):
                del groups[i]
                del groups[start]
                ans+=1
            else:
                start+=1
        start=0
        while(start<len(groups)):
            i=-1
            j=-1
            val=-1
            for i in range(start+1,len(groups)):
                for j in range(i+1,len(groups)):
                    val=(groups[start]+groups[i]+groups[j])%chocolateInPackage
                    if(val==0):
                        break
                if (val==0):
                    break
            if (val==0):
                del groups[j]
                del groups[i]
                del groups[start]
                ans+=1
            else:
                start+=1
        start=0
        while (start < len(groups)):
            i = -1
            j = -1
            k= -1
            val = -1
            for i in range(start + 1, len(groups)):
                for j in range(i + 1, len(groups)):
                    for k in range(j+1,len(groups)):
                        val = (groups[start] + groups[i] + groups[j]+groups[k]) % chocolateInPackage
                        if (val == 0):
                            break
                    if (val == 0):
                        break
                if (val == 0):
                    break
            if (val == 0):
                del groups[k]
                del groups[j]
                del groups[i]
                del groups[start]
                ans += 1
            else:
                start += 1

        if(len(groups)>0):
            ans+=1
        self.result=ans




f = open(inputFile,"r")

firstLine = f.readline()
numberOfWords = int(firstLine)
print(numberOfWords)
o = open(outFile, "w")
i=0
for wordNumber in range(numberOfWords):
    i+=1
    d = A(f)
    print("Case #{0}: {1}".format(i,d.result))

    o.write( "Case #{0}: {1}\n".format(i,d.result))
