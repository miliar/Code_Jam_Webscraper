def tidyNumbers(number):

    if len(number) == 1:
        return number
    else:
        listNumber = []
        for digits in number:
            listNumber.append(int(digits))

        for i in range(len(listNumber)-1):

            if listNumber[i] <= listNumber[i+1] :
                pass
            else:
                numbers = int(number)-1
                return tidyNumbers(str(numbers))
        return number





testCase = int(input())
for i in range(testCase):
    number = input()
    print("Case #%i:" %(i+1),tidyNumbers(number))
