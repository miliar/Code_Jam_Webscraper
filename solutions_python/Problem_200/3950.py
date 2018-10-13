def tiddy(number):
    outOfOrder = True
    while outOfOrder:
        listNumber = []
        for digit in str(number):
            listNumber.append(digit)
        listNumber.sort()
        numberString = "".join(listNumber)
        if (number == int(numberString)):
            outOfOrder = False
            return number
        else:
            number -= 1
def main():
    testCases = int(input())
    for i in range(1, testCases + 1):
        number = int(input())
        print("Case #{}: {}".format(i, tiddy(number)))

main()








