f = open("A-small-attempt0.in", "r")
n = int(f.readline())
ans = []
for i in range(n):
    num1 = int(f.readline())
    mat1 = []
    for i in range(4):
        line = f.readline()
        list1 = line.split(" ")
        for index, value in enumerate(list1):
            list1[index] = int(value)
        mat1.append(list1)
    num2 = int(f.readline())
    #print mat1
    mat2 = []
    for i in range(4):
        line = f.readline()
        list1 = line.split(" ")
        for index, value in enumerate(list1):
            list1[index] = int(value)
        mat2.append(list1) 
    #print mat2
    cnt = 0
    #print num1, num2
    for i in mat1[num1-1]:
        if i in mat2[num2-1]:
            cnt += 1
            a = i
    if cnt == 1:
        ans.append(a)
    elif cnt == 0:
        ans.append("Volunteer cheated!")
    elif cnt > 1:
        ans.append("Bad magician!")
f.close()
f = open("output.txt", "w")
for index, value in enumerate(ans):
    f.write("Case #"+str(index+1)+": "+str(value)+"\n")
f.close()
