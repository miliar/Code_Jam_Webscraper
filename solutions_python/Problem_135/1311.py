
f = open('input.txt')

t = int(f.readline())
output = [0]*t

for i in range(t):
    r1 = int(f.readline()) - 1
    g1 = [[0]*4]*4
    for j in range(4):
        temp = f.readline()
        temp = temp.split()
        g1[j] = [int(x) for x in temp]
    r2 = int(f.readline()) - 1
    g2 = [[0]*4]*4
    for k in range(4):
        temp = f.readline()
        temp = temp.split()
        g2[k] = [int(x) for x in temp]
    x1 = g1[r1]
    x2 = g2[r2]
    count = 0
    elem = -1
    for n in x1:
        if n in x2:
            count += 1
            elem = n
    if count == 1:
        output[i] = str(elem)
    if count == 0:
        output[i] = "Volunteer cheated!"
    if count > 1:
        output[i] = "Bad magician!"

f.close()

f = open("output.txt", "w")

for i, o in enumerate(output):
    f.write("Case #" + str(i+1) + ": " + o + "\n")

f.close()
