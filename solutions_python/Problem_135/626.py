my_file = open('Input.txt',"r")
my_file2 = open('Output.txt', "w")
N = int(my_file.readline())
for i in range(1,N+1):
    a = int(my_file.readline())
    b = []
    for x in range(1,5):
        b.append(my_file.readline().split())
    c = int(my_file.readline())
    d = []
    for x in range(1,5):
        d.append(my_file.readline().split())
    t = b[a-1]
    k = d[c-1]
    cnt = 0
    same = -1
    for x in t:
        for y in k:
            if x==y:
                same = x
                cnt += 1
    if cnt == 1:
        my_file2.write("Case #"+str(i)+": "+str(same)+"\n")
    elif cnt == 0:
        my_file2.write("Case #"+str(i)+": Volunteer cheated!"+"\n")
    else:
        my_file2.write("Case #"+str(i)+": Bad magician!"+"\n")
my_file.close()
my_file2.close()