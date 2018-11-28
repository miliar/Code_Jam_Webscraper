import sys
def main():
    file="tidyNumbers.txt"
    opened_file=open(file)
    numberOfCases=opened_file.readline()
    numberOfCases=int(numberOfCases)
    for i in range(numberOfCases):
        singleDigitChecker=False
        current_number=opened_file.readline()
        current_number=int(current_number)
        counter=0
        while counter<=current_number:
            numberOfSuccesses=0
            numberOfDigits=len(str(current_number))
            if numberOfDigits==1:
                print("Case #"+str(i+1)+":",current_number)
                singleDigitChecker=True
                break
            for j in range((len(str(counter))-1)):
                if (str(counter))[j]<=(str(counter))[j+1]:
                    numberOfSuccesses+=1
                    if numberOfSuccesses==(len(str(counter))-1):
                        current_max=counter
                else:
                    break

            counter+=1
        if singleDigitChecker==False:
            print("Case #"+str(i+1)+":",current_max)

main()