def conCont(word , con):
    streak = 0
    for x in word:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            streak = 0
        else:
            streak += 1
        if streak == con:
            return True
    return False
f = open("DATA1.txt")
g = open("OUT1.txt",'w')
n = f.readline().strip()
for x in range(int(n)):
    i = f.readline().strip().split(" ")
    counter = 0
    for y in range(len(i[0])):
        if y >= int(i[1]):
            for z in range(len(i[0]) - y +1):
                if conCont(i[0][z:z+y],int(i[1])):
                    counter += 1
    if conCont(i[0], int(i[1])):
        counter +=1
        print(i[0])
    g.write("Case #"+str(int(x+1))+": "+str(counter)+"\n")
g.close()
