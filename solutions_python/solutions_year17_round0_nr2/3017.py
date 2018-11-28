def getTidyNumber(number):
    n = len(number) - 1
    x = [n for n in number]
    tidyNumber = 0

    for i in range(n):
        if int(x[i]) > int(x[i+1]):
            x[i] = str(int(x[i]) - 1)
            for j in range(i+1,len(x)):
                x[j] = '9'
    
    for i in range(n,0,-1):
        num1 = int(x[i])
        num2 = int(x[i-1])
        if num2 > num1:
            x[i] = '9'
            x[i-1] = str(num2 - 1)
    tidyNumber = int(''.join(x))
    return tidyNumber

            
with open('B-large.in','r') as f, open('outputTidyL.txt','w') as o:
    first = True
    caseNum = 0
    for line in f:
        if first:
            first = False
            continue
        result = getTidyNumber(str.strip(line))
        o.write('Case #{0}: {1}\n'.format(caseNum+1, result))
        #print(('Case #{0}: {1}\n'.format(caseNum+1, result)))
        caseNum += 1
    print('Done')