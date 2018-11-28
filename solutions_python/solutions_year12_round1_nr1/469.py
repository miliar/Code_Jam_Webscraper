'''
Created on 2012-4-28

@author: yao
'''

if __name__ == '__main__':
    f = open("A-small-attempt0.in")
    data = f.readlines()
    f.close()
    casenum = int(data[0])
    for case in range(1, casenum+1):
        temp = data[case*2-1].split(" ")
        A = int(temp[0])
        B = int(temp[1])
        temp = data[case*2].replace("\n","").split(" ")
        plist = []
        for each in temp:
            plist.append(float(each))
        mintry = float(B+2.0)
        ptemp = float(1.0)
        for each in plist:
            ptemp *= each
        mintry = min(mintry, ptemp*(B-A+1)+(1-ptemp)*(B-A+B+2))
        for i in range(1, A+1):
            ptemp = float(1.0)
            for j in range(0, A-i):
                ptemp *= plist[j]
            mintry = min(mintry, ptemp*(B-A+1+2*i) + (1-ptemp)*(B-A+2+B+2*i))
        print "Case #%d: %0.6f" % (case, mintry)