file = open("B-large.in","r")
numbers = []
for line in file:
    line = line.strip()
    numbers.append(line)
numbers = numbers[1:]
tidy = []

##def check(value):
##    var = str(value)
##    array = []
##    for i in var:
##        array.append(i)
##    for j in range(len(array) - 1):
##        x = int(j)
##        x = array[j]
##        y = array[j + 1]
##        if x <= y:
##            pass
##        else:
##            value = int(value) - 1
##            return check(value)
##    return value

def check(value):
    var = str(value)
    array = []
    for i in var:
        array.append(i)
    for j in range(len(array) - 1):
        x = int(j)
        x = array[j]
        y = array[j + 1]
        if x <= y:
            pass
        else:
            array[j] = int(array[j]) - 1
            for i in range(j + 1,len(array)):
                array[i] = 9
            value = ''.join(str(i)for i in array)
            return check(value)
    if value[0] == '0':
        value = value[1:]
    return value

for num in numbers:
    if len(num) == 1:
        tidy.append(num)
    else:
        tidied = check(num)
        tidy.append(tidied)
file.close()

file = open("final2.txt","w")
for i in range(len(tidy)):
    file.write("Case #{0}: {1}\n".format(i + 1,tidy[i]))
file.close()
        
        
