def main():
    T = int(input())
    for t in range(1,T+1):
        numberString = input()
        tidyNo(str(numberString),t)
def tidyNo(numberString,t):

    numberInteger = int(numberString)
    numberArrayForm = []
    powerOfTen=0
    # print(numberInteger)
    if(numberInteger < 10):
        # print("Do stuff for Single Integer")
        print("Case #"+str(t)+": "+str(numberInteger))
        return
    else:
        # print("Do Stuff for general integer")
        for n in str(numberInteger):
            numberArrayForm.append(n)
        if numberInteger % 10 == 0:
            # print("Case #"+str(t)+": "+str(numberInteger-1))
            # return
            tidyNo(str(numberInteger-1),t)
            return
        # print(numberArrayForm)
        for n in range(0,len(numberArrayForm)-1):
            # print(n)
            if numberArrayForm[n] > numberArrayForm[n+1]:
                # print("Galat hai ye number")
                powerOfTen=len(numberArrayForm)-n-1
                # print(pow(10,powerOfTen))
                computedNumber = numberInteger - numberInteger%pow(10,powerOfTen) - 1
                sahiHai = checker(str(computedNumber))
                if sahiHai:
                    print("Case #"+str(t)+": "+str(computedNumber))
                    return
                else:
                    tidyNo(str(computedNumber),t)
                    return
        sahiHai = checker(str(numberInteger))
        if sahiHai:
            print("Case #"+str(t)+": "+str(numberInteger))
        else:
            tidyNo(str(numberInteger),t)
            return
def checker(number):
    for n in range(0,len(number)-1):
        if number[n] > number[n+1]:
            return False
    return True
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
