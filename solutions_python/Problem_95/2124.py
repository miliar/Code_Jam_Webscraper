InFile = open("input1.in","r")
OutFile = open("output1.out","w")
TestCases = int(InFile.readline())
#rpList = ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','3']
TestS1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv q z"
TestS2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up z q"
for casenum in range(0,TestCases):
    CurLine = InFile.readline()
    OutS = ""
    for letter in CurLine:
       # print letter
        if ((letter >= 'a') and (letter <= 'z')) or (letter == ' '):
            
            ind = TestS1.index(letter)
            
            OutS += TestS2[ind]
        else:
            OutS += letter
    OutFile.write("Case #" + str(casenum+1)+": " + OutS)


InFile.close()
OutFile.close()
