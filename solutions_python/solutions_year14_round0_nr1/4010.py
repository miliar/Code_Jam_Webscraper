'''
Created on 2014-4-13

@author: min
'''
case1 = r'Case #%d: %s'
case2 = r'Case #%d: Bad magician!'
case3 = r'Case #%d: Volunteer cheated!'

def findRes(infos1, infos2, index):
    count = 0
    text = ''
    for num in infos1:
        for num2 in infos2:
            if num2 == num:
                count = count + 1
                text = num
    
    res = ''
    if count == 1:
        res = case1 %(index, text)
    elif count > 1:
        res = case2 %index
    else:
        res = case3 %index
    return res

def printResult(bfList, index):
    row1 = int(bfList[0])
    infos1 = bfList[row1].split()
    row2 = int(bfList[5])
    infos2 = bfList[row2 + 5].split()
    return findRes(infos1, infos2, index)

if __name__ == '__main__':
    fp = open('1-input.txt', 'r')
    outputFp = open('1-output.txt', 'w')
    count = 0
    bfList = []
    for line in fp.readlines():
        if not line:
            continue
        if count > 0:
            bfList.append(line.strip())
            if count % 10 == 0:
                res = printResult(bfList, count/10)
                outputFp.write(res + '\n')
                bfList = []
        count = count + 1
    fp.close()
    outputFp.close()