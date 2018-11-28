opdracht = open('testfile.in')
caselist = []
for lines in opdracht:
    print(lines)
    caselist.append(lines.rstrip())
cases = caselist.pop(0)
print (cases)
print (caselist)

def recurseadapt(intlist, digit):
    if intlist[digit] != 0:
        intlist[digit] -= 1
        return intlist
    else:
        if digit != 0:
            intlist[digit] = 9
            recurseadapt(intlist, digit-1)

resultlist = []
for i in caselist:
    #convert to list
    digits = list(i)
    for j in range(len(digits)):
        digits[j] = int(digits[j])
    amount = len(digits)
    current = amount-1
    print(current)
    print (digits)
    #compare numbers
    while current > 0:
        preceding = current - 1
        #if not tidy
        if digits[current] < digits[preceding]:
            #adapt to 9's
            for j in range (current, amount):
                digits[j] = 9
            #lower preceding
            recurseadapt(digits, current-1)
        current -= 1

    while digits[0] == 0:
        digits.pop(0)
        print(digits)
    for j in range(len(digits)):
        digits[j] = str(digits[j])
    digits = ''.join(digits)
    resultlist.append(digits)

resultaat = open('resultaat', 'w')
for i in range(len(resultlist)):
    digits = 'Case #'+str(i+1)+': '+str(resultlist[i])+'\n'
    resultaat.write(digits)
