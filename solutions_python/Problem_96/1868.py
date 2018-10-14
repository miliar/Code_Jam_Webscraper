import glob, time, string, re
textFile = open("B-output_small.txt", "w")
#textFile = open("B-output_large.txt", "w")
sInputFileLoc = 'B-small-attempt4.in'
#sInputFileLoc = 'B-large-practice.txt'
sInputFile = open(sInputFileLoc, "r")
sLineOutput = "Case #"
iLineRead = 0

iNumTestCases = int(sInputFile.readline())


for xx in range(iNumTestCases):
    sInputString = sInputFile.readline()
    aInputData = sInputString.split()
    iNumberOfGooglers = 0 #greater than P
    print("Case #" + str(xx+1))
    print("Surpries == " + aInputData[1])
    for x in range(int(aInputData[0])):
#        print("P=" + (aInputData[2]))
        print("S=" + (aInputData[3+x]))
        if (int(aInputData[3 + x])/3)+1 >= int(aInputData[2]) and not float(int(aInputData[3 + x])/3).is_integer() :
            print("1")
#            print((int(aInputData[3 + x])/3))
            iNumberOfGooglers = iNumberOfGooglers + 1
        elif (int(aInputData[3 + x])/3) >= int(aInputData[2]):
            print("2")
#            print((int(aInputData[3 + x])/3))
            iNumberOfGooglers = iNumberOfGooglers + 1
        elif (int(aInputData[1]) != 0 )and((int(aInputData[3 + x])/3)+2) >= int(aInputData[2])and ((int(aInputData[3 + x]) != 0))and ((int(aInputData[3 + x])/3)+2) <= int(aInputData[3 + x]):
            print("3")
#            print("(*)" + str((int(aInputData[3 + x])/3)))
            aInputData[1] = str(int(aInputData[1]) - 1)
            iNumberOfGooglers = iNumberOfGooglers + 1
        else:
            print("4")
#            print("Case #" + str(xx+1))
#            print("Surpries == " + aInputData[1])
#            print("P=" + (aInputData[2]))
#            print((int(aInputData[3 + x])/3))
#            print("S=" + (aInputData[3+x]))
#            print("NONE")
    print("Max Number - " + str(iNumberOfGooglers)            )
    print("-*-*-*-*-*-*-*-*-*")

    textFile.write(sLineOutput+str(xx+1)+ ": ")    
    textFile.write(str(iNumberOfGooglers))
    sTempLast = ""

    textFile.write("\n")    
textFile.close()
sInputFile.close()
