def countEm(inputText):
    splitText = inputText.split()
    numberOfGooglers = int(splitText.pop(0))
    numberOfSuprising = int(splitText.pop(0))
    threshold = float(splitText.pop(0))
    
    count = 0
    suprisingCount = 0
    
    for number in splitText:
        number = float(number)
        result = number/3

        
        
        if number >= 3*threshold - 2:
            #not a suprising result
            count = count + 1
        elif number >= 3*threshold - 4 and suprisingCount < numberOfSuprising and number >= 2:
            #potential suprising result
            count = count + 1
            suprisingCount = suprisingCount + 1

    return str(count)

def runTest():
    f = open('/Users/bavetta/Desktop/code jam/dance/B-large (1).in', 'r')
    numberOfLines = int(f.readline())
    
    for i in range(numberOfLines):
        output = ["Case #"]
        output.append(str(i+1))
        output.append(": ")

        
        input = f.readline()
        output.append(countEm(input))
        output = ''.join(output)

        print(output)


runTest()
