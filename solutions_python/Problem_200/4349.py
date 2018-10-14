def main():
    testCases = int(input())
    for testCase in range(1,testCases+1):
        numberString = input()
        printTidyNumber(str(numberString),testCase)
def printTidyNumber(numberString,testCase):

    numberInteger = int(numberString)
    numberArrayForm = []
    powerOfTen=0
    # print(numberInteger)
    if(numberInteger < 10):
        # print("Do stuff for Single Integer")
        print("Case #"+str(testCase)+": "+str(numberInteger))
        return
    else:
        # print("Do Stuff for general integer")
        for n in str(numberInteger):
            numberArrayForm.append(n)
        if numberInteger % 10 == 0:
            # print("Case #"+str(testCase)+": "+str(numberInteger-1))
            # return
            printTidyNumber(str(numberInteger-1),testCase)
            return
        # print(numberArrayForm)
        for n in range(0,len(numberArrayForm)-1):
            # print(n)
            if numberArrayForm[n] > numberArrayForm[n+1]:
                # print("Galat hai ye number")
                powerOfTen=len(numberArrayForm)-n-1
                # print(pow(10,powerOfTen))
                computedNumber = numberInteger - numberInteger%pow(10,powerOfTen) - 1
                sahiHai = sahiHaiKya(str(computedNumber))
                if sahiHai:
                    print("Case #"+str(testCase)+": "+str(computedNumber))
                    return
                else:
                    printTidyNumber(str(computedNumber),testCase)
                    return
        sahiHai = sahiHaiKya(str(numberInteger))
        if sahiHai:
            print("Case #"+str(testCase)+": "+str(numberInteger))
        else:
            printTidyNumber(str(numberInteger),testCase)
            return
def sahiHaiKya(number):
    for n in range(0,len(number)-1):
        if number[n] > number[n+1]:
            return False
    return True
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
