
def getTime(dc, dx):
    return dx/dc

file = open('input.txt')

t = int(file.readline())
output = [0]*t

for i in range(t):
    temp = file.readline()
    temp = temp.split()
    c,f,x = float(temp[0]), float(temp[1]), float(temp[2])
    totalTime = 0
    r = 2
    while(True):
        if getTime(r, x) > (getTime(r, c) + getTime(r + f, x)):
            totalTime += getTime(r,c)
            r += f
        else:
            totalTime += getTime(r, x)
            break
    output[i] = str(totalTime)

file.close()

file = open('output.txt', 'w')

for i, o in enumerate(output):
    file.write("Case #" + str(i+1) + ": " + o + "\n")

file.close()

