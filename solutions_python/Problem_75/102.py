#!/usr/bin/python -tt

import sys

def main():
    inFile = open(sys.argv[1], 'rU')
    outFile = open(sys.argv[2], 'w')
    aLine = inFile.readline()
    T = eval(aLine)
    for case in range(T):
        cDic = {}
        oDic = {}
        aLine = inFile.readline()
        aLine = aLine.split()
        C = eval(aLine.pop(0))
        for i in range(C):
            rule = aLine.pop(0)
            cDic[rule[0] + rule[1]] = rule[2]
            cDic[rule[1] + rule[0]] = rule[2]
        print cDic
        D = eval(aLine.pop(0))
        for i in range(D):
            rule = aLine.pop(0)
            oDic[rule[0] + rule[1]] = True
            oDic[rule[1] + rule[0]] = True
        print oDic
        N = eval(aLine.pop(0))
        aLine = aLine.pop(0)
        ans = []
        for i in range(N):
            ans.append(aLine[i])
            if len(ans) >= 2:
                s = ans[-1] + ans[-2]
                if s in cDic:
                    ans.pop()
                    ans.pop()
                    ans.append(cDic[s])
                for j in range(len(ans)-1):
                    s = ans[-1] + ans[j]
                    if s in oDic:
                        ans = []
                        break
        print "ans = ", ans
        if len(ans) == 0:
            outFile.write("Case #%d: []\n" % (case+1))
            continue
        outFile.write("Case #%d: [%s" %(case+1, ans[0]))
        for i in range(1, len(ans)):
            outFile.write(", %s" % ans[i]);
        outFile.write("]\n")
    inFile.close()
    outFile.close()


if __name__ == '__main__':
    main()
