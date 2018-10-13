from math import sqrt
Input = open(raw_input("Enter Input Path:"))
InputList = []
for line in Input:
    InputList.append(line[:-1])

Input.close()
InputList.pop(0)
OutputList = []
def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

caseNum = 0
for case in InputList:
    caseNum+=1
    FairSquares = 0
    A = int(case.split()[0])
    B = int(case.split()[1])
    palindromes = []
    for num in range(A,B+1):
        if str(num) == str(num)[::-1]:
            palindromes.append(num)
    palindromeSquares=[]
    for num2 in palindromes:
        sqrtnum2 = sqrt(num2)
        sqrtnum2-=int(sqrtnum2)
        if sqrtnum2 == 0.0:
            palindromeSquares.append(int(sqrt(num2)))
    for num3 in palindromeSquares:
        if str(num3) == str(num3)[::-1]:
            FairSquares += 1
    OutputList.append("Case #" + str(caseNum) + ": " + str(FairSquares))

Output = open(raw_input("Enter Output Path:"), "wb")
for caseline in OutputList:
    Output.write(caseline + "\r\n")

Output.close()