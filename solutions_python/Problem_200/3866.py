def isTidy(number):
    aux = str(number)
    extenso = [x for x in aux]
    if(extenso == sorted(extenso)):
        return True
    else:
        return False

"""def check(number, digits):
    aux = str(number)
    if(digits == len(aux)):
        first = aux[0]

    else:
        digits -= 1
        aux = ""
        for i in range(digits):
            aux += '9'
        return int(aux)"""

testcases = int(input())

for i in range(testcases):
    number = int(input()) + 1
    tidy = 1
    for j in range(1, number):
        if(isTidy(j) == True):
            tidy = j
    print('Case #{0}: {1}'.format(i + 1, tidy))
