
#input1 = open(r"c:\googleCode\candytest.txt")
input1 = open(r"c:\googleCode\c-large.in")
output1 = open(r"c:\googleCode\candylarge.txt", 'w')
lines = input1.readline()
T = int(lines.strip())
lines = input1.readline()
caseN =1
while lines !='':
    lines = input1.readline()
    can = lines.split(' ')
    canI = []
    for key in can:
        temp = int(key)
        canI.append(temp)
    total = 0
    canI.sort()
    for key in canI:
        total = total^key

    x = "Case #"+ str(caseN)+": "
    caseN +=1
    sean =0
    if total !=0:
        x += "NO\n"
    else:
        for key in canI[1:]:
            sean +=key
        x += str(sean)+'\n'
    print(x)
    output1.write(x)    
    lines = input1.readline()

input1.close()
output1.close()
