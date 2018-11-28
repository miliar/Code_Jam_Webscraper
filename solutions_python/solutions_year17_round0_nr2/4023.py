
total = 0
case = 1

knowNumbers = []

#entrenaimeinto inicial
i=1
number = 999999999999999999
while i < number+1 :
    numberList = map(long,list(str(i)))

    for j in range(0,len(numberList)):

        if len(numberList) == 1 :

            knowNumbers.append(i)
            i = i + 1
            break
        elif j > 0 and numberList[j] < numberList[j - 1]:
            
            numberList[j] = numberList[j -1]
            i = long(''.join(str(e) for e in numberList))
            break
        elif j == len(numberList) - 1:

            knowNumbers.append(i)
            i = i + 1
            break

print "size kn: "+str(len(knowNumbers))

print "fin entrenamiento!!"
raw_input()

file = open("input.txt","r")
out = open("out.txt", "w")

n = int(file.readline())
print "cases: "+str(n)

for line in file:
    
    lastNumber = 0
    line = line.rstrip('\n')
    
    number = long(line)
    

    for limit in knowNumbers:
        if limit <= number:
            lastNumber = limit
        else:
            break
    
    print "last number "+str(lastNumber)

    out.write("Case #"+str(case)+": "+str(lastNumber)+"\n") 
    case = case + 1

file.close()
out.close()







