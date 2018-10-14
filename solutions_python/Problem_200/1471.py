def isMess(L):
    for i in range(0,len(L)-1):
        if L[i+1]<L[i]:
            return i
    return -1


def tidy(num):
    array = list(str(num))
    check = isMess(array)
    while check != -1:
        array[check] = str(int(array[check])-1)
        for i in range(check+1,len(array)):
            array[i] = '9'
        check = isMess(array)
    tidy = int(''.join(array))
    print(tidy)
    return tidy

with open('problemBBig.txt', 'r') as file:
    array = []
    for line in file:
        if line != '':
            array.append(line.replace('\n',''))
    array = array[1:]
    print(array)

with open('problemBBigsoln.txt','w',encoding='utf-8') as file:
    file.write('')
    for t,case in enumerate(array):
        file.write('Case #'+str(t+1)+': ' + str(tidy(int(case))) + '\n')
