text = open("small.txt", "rb")
n = int(text.readline().strip("\n"))
for i in range(n):
    rownum1 = int(text.readline().strip("\n"))
    for j in range(4):
        line = text.readline().strip("\n")
        if(j == rownum1 - 1):
            row1 = [int(num) for num in line.split()]
    rownum2 = int(text.readline().strip("\n"))
    for j in range(4):
        line = text.readline().strip("\n")
        if(j == rownum2 - 1):
            row2 = [int(num) for num in line.split()]
    count = 0
    for num in row1:
        if num in row2:
            count+=1
            record = num
    output = open("answer.txt", "a")
    if(count == 0):
        output.write("Case #" + str(i + 1) + ": Volunteer cheated!\n")
    elif(count == 1):
        output.write("Case #" + str(i + 1) + ": " + str(record) +"\n")
    else:
        output.write("Case #" + str(i + 1) + ": Bad magician!\n")
text.close()
output.close()
