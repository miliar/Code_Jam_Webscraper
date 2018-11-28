inputF = open('B-large.in', 'r')
output = open('B-large.out', 'w')


def findTidyNum(num):
    if isTidy(num):
        return num
    strNum = str(num)
    subtraction = (num % 10) + 1
    for i in range(1,len(strNum)+1):
        if isTidy(num-subtraction):
            return num-subtraction
        subtraction += int(strNum[-1*(i+1)])*(10**i)
    

def isTidy(num):
    strNum = str(num)
    for i in range(len(strNum)-1):
        if strNum[i] > strNum[i+1]:
            return False
    return True

numCases = int(inputF.readline())

for i in range(numCases):
    num = int(inputF.readline())
    
    num = findTidyNum(num)

    output.write('Case #' + str(i+1) + ': ')
    output.write(str(num) + '\n')

inputF.close()
output.close()
