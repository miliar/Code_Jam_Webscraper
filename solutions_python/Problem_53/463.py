f = open('A-large.txt', 'r')
w = open('Output.txt', 'w')

cases = f.readline()

cases = int(cases)

for i in range(0, cases):
    line = f.readline()
    numArr = str.split(line, " ")
    
    n = int(numArr[0])
    k = int(numArr[1])
    
    expectedAnswer = (2 ** n) - 1

    answer = ""
    
    if k % (2 ** n) == expectedAnswer:
        answer = "ON"
    else:
        answer = "OFF"
        
    w.write("Case #" + str(i + 1) + ": " + answer + "\n")
    
f.close()
w.close()

print "DONE"
