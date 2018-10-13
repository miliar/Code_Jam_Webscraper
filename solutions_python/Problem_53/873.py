input = open('A-large.in','r')
output = open('A-large.out','w')

testcases = input.readline()
cases = 1
for x in range(int(testcases)):
    temp = input.readline()
    inputList = temp.split()
    if (int(inputList[1]) == 0):
        output.write("Case #" + str(cases) + ": OFF" + '\n')
        cases+=1
    else:
        if ((int(inputList[1]) + 1) % 2**(int(inputList[0])) == 0):
            output.write("Case #" + str(cases) + ": ON" + '\n')
            cases+=1
        else:
            output.write("Case #" + str(cases) + ": OFF" + '\n')
            cases+=1
output.close()
