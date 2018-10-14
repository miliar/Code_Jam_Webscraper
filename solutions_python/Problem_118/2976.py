import math
def fs(a,b):
    global summ
    summ = 0
    for j in range(a,b+1):
        if (str(j))[::-1] == str(j):
            if math.sqrt(j) % 1 == 0:
                x = str(int(math.sqrt(j)))
                if x[::-1] ==str(str(int(math.sqrt(j)))):
                    summ = summ + 1
    return (summ)

infile = open("C-small-attempt0.IN", 'r')
outfile = open("C-small",'w')
lines = infile.readlines()
num = []

i = 1
for line in lines:
    if i != len(lines):
        num.append(line[:-1])
        i += 1
    else:
        num.append(line)

num.pop(0)
space = []
for i in num:
    posn = 0
    for j in i:
        if j == ' ':
            space.append(posn)
            break
        else:
            posn += 1

#print(num)

position = 0
for i in num:
    x = space[position]
    a = int(i[0:x])
    b = int(i[x:])
    fs(a,b)
    position += 1
    outfile.write("Case #" + str(position) + ": "+ str(summ) + '\n')




infile.close()
outfile.close()
