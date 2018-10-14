
filename = 'B-small-attempt1.in'
outputname = 'output.txt'
file = open(filename, 'r')
first = 0
n = int(file.readline())
output = []
for i in range(n):
    line = file.readline()
    t = int(line)
    for j in range(t):
        k = t-j
        check = False
        num = str(k)
        prev = 0
        for char in num:
            if int(char) >= prev:
                check = True
                prev = int(char)
            else:
                check = False
                break
        if check:
            output.append('Case #' + str(i+1) + ": " + str(k) + "\n")
            break

file.close()
newfile = open(outputname, 'w')
newfile.writelines(output)
newfile.close()
