f = open("A-large.in","r")
data = []
for line in f:
    data.append(line.strip())
f.close()
for i in range(1,len(data)):
    current = []
    data[i] = data[i].split(" ")
    flipper = int(data[i][1])
    for j in range(len(data[i][0])):
        if data[i][0][j] == "+":
            current.append(0)
        else:
            current.append(1)
    count = 0
    for j in range(len(current)):
        if current[j]%2 == 1:
            if len(current) - j < flipper:
                print("Case #"+str(i)+": "+"IMPOSSIBLE")
                break
            else:
                count += 1
                for k in range(j,j+flipper):
                    current[k] -= 1
        else:
            if j == len(current) - 1:
                print ("Case #"+str(i)+": "+str(count))
                break
            continue
