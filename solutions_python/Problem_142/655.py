import math

#any functions here

#main here
infile = open("A-small-attempt4.in", "r")
outfile = open("Aout.txt", "w")
t = int(infile.readline().rstrip())
for z in range(1, t+1):
    #IO here
    number = int(infile.readline())
    inputs = []
    for i in range(0, number):
        inputs.append(infile.readline().rstrip())
    inputs = sorted(inputs)
    letters=[]
    for i in range(1, len(inputs[0])):
        if inputs[0][i]!=inputs[0][i-1]:
            letters.append(inputs[0][i])
    #compare
    possible=True
    if len(letters)>0:
        for i in range(1, len(inputs)):
            current=0
            for j in range(1, len(inputs[i])):
                if inputs[i][j]!=inputs[i][j-1]:
                    if current>=len(letters):
                        possible=False
                        break
                    if letters[current]!=inputs[i][j]:
                        possible=False
                        break
                    current+=1
            if current!=len(letters):
                possible=False
    first = inputs[0][0]
    for i in range(len(inputs)):
        if inputs[i][0]!=first:
            possible=False
    if possible==False:
        solution="Fegla Won"
    else:
        numbers=[]
        for i in range(0, len(inputs)):
            current=[]
            count=1
            for j in range(1, len(inputs[i])):
                if inputs[i][j]!=inputs[i][j-1]:
                    current.append(count)
                    count=1
                else:
                    count+=1
            current.append(count)
            numbers.append(current)
        solution=0
        '''for i in range(0, len(numbers[0])):
            if numbers[0][i]>numbers[1][i]:
                solution+=(numbers[0][i]-numbers[1][i])
            else:
                solution+=(numbers[1][i]-numbers[0][i])'''
        for i in range(0, len(numbers[0])):
            total=0
            for j in range(0, len(numbers)):
                total+=numbers[j][i]
            average = int(total/len(numbers))
            for j in range(0, len(numbers)):
                if numbers[j][i]>average:
                    solution+=numbers[j][i]-average
                elif average>numbers[j][i]:
                    solution+=average-numbers[j][i]
    output = "Case #"+str(z)+": " + str(solution) + "\n"
    print(output)
    outfile.write(output)

infile.close()
outfile.close()
