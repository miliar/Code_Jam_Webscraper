fileName = input("File Name: ")
if fileName == "":
    fileName = "A-large"
file1 = open(fileName + ".in")
file2 = open(fileName + ".out", "w")

T = int(file1.readline())
for i in range(1, T + 1):
        D, N = [int(s) for s in file1.readline().split()]
        listaCaballos = list()
        for j in range(N):
            Ki, Si = [int(s) for s in file1.readline().split()]
            listaCaballos.append((Ki, Si))
        print(listaCaballos)
        listaCaballos.sort()
        listaCaballos.reverse()
        
        time = None
        for caballo in listaCaballos:
            if time == None:
                time = (D - caballo[0]) / caballo[1]
            else:
                if (D - caballo[0]) / caballo[1] > time:
                    time = (D - caballo[0]) / caballo[1]

        answer = D / time
            
        print("Case #{}: {}".format(i, answer))
        file2.write("Case #{}: {}\n".format(i, answer))

file1.close()
file2.close()
