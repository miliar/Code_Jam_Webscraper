
FILE_NAME = 'C-small-attempt1.txt'


def numPalindrome(num, check = True):

    #Decimal Check
    if check:
        if str(num).find('.') > -1:
            if num - int(str(num)[:str(num).find('.')]) == 0:
                return numPalindrome(str(num)[:str(num).find('.')])
            else:
                return numPalindrome(num,False)

    if str(num) == str(num)[::-1]:
        return True
    return False


numCases = 0
testCases = []
with open(FILE_NAME,'r') as file:
    numCases = file.readline()
    for line in file:
        a,b = line.split()
        testCases.append((int(a),int(b)))


caseNum = 1

with open('results.txt','w') as file:
    for case in testCases:
        total = 0
        for num in xrange(case[0],case[1]+1):
            if numPalindrome(num):
                if numPalindrome(num**.5):
                    total += 1
        file.write('Case #{}: {}\n'.format(caseNum,total))
        caseNum += 1


        
    
    
            
