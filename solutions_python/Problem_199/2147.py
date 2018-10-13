import sys

def answer(inputs):
    s = inputs[0]
    k = int(inputs[1])
    sLen = len(s)

    ans = 0

    for i, pancake in enumerate(s[:-k + 1]):
        if s[i] == '-':
            for i2 in range(i, i+k):
                if s[i2] == '-':
                    s = s[:i2] + '+' + s[i2+1:]
                else:
                    s = s[:i2] + '-' + s[i2+1:]
            ans += 1

    for pancake in s[sLen-k:]:
        if pancake == '-':
            ans = 'IMPOSSIBLE'
            break
    
    return str(ans)


filename = input("Enter filename: ")

with open(filename, 'r') as inputFile:
    with open(filename + '_out.o', 'w') as outputFile:
        sys.stdout = outputFile
        testCaseNum = int(inputFile.readline().replace('\n',''))

        for i in range(1, testCaseNum + 1):
            inputs = (inputFile.readline().replace('\n','')).split(' ')
            ans = answer(inputs)
            print("Case #" + str(i) + ": " + ans)
