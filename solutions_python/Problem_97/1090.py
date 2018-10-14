fob = open("c:/inputs/codejam/C-small-practice.in",'r')
fob2 = open("c:/inputs/codejam/C-small-practice.out",'w')
numTest = int(fob.readline())
i = 0
glue = ''
form = "Case #%s: "
while i < numTest:
    numbers = (fob.readline()).split()
    maxA = int(numbers[0])
    maxB = int(numbers[1])
    count = 0
    j = maxA
    while j <= maxB:
        k = 0
        m = j
        newList = list(str(j))
        length = len(newList)
        done = []
        while k < length:
            if m >= maxA and m <=maxB and m > j:
                if m not in done:
                    count = count + 1
                    done.append(m)
            newList = newList[1:] + newList[0:1]
            m = int(glue.join(newList))
            k = k + 1
        j = j + 1
    fob2.write(form % (str(i+1))+ str(count)+ '\n')             
    i = i + 1
fob.close()
fob2.close()
            
        
        
