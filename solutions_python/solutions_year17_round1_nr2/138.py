from math import ceil, floor

fileName = input("File Name: ")
if fileName == "":
    fileName = "B-large.in"
file1 = open(fileName)
file2 = open("sol_" + fileName, "w")

def getUnits(total, each):
    #print("{}/{}".format(total, each))
    listSalida = list()
    for i in range(ceil(total / (each * 1.1)), floor(total / (each * 0.9)) + 1):
        if total >= each * i * 0.9 and total <= each * i * 1.1:
            listSalida.append(i)
    #print(listSalida)
    return listSalida

T = int(file1.readline())
for i in range(1, T + 1):
    N, P = [int(s) for s in file1.readline().split()]
    R = [int(s) for s in file1.readline().split()]
    Q = list()
    for n in range(N):
        Q.append([int(s) for s in file1.readline().split()])

    for quantities in Q:
        quantities.sort()

    #print("R: {}".format(R))
    #print("Q: {}".format(Q))
    answer = 0
    for paquete in Q[0]:
        unidades = getUnits(paquete, R[0])
        for unidad in unidades:
            paquetesEliminar = list()
            #print("---")
            #print("{}: {}".format(paquete, unidad))
            for nIng in range(1, N):
                for paquete2 in Q[nIng]:
                    if paquete2 <= unidad * R[nIng] * 1.1 and paquete2 >= unidad * R[nIng] * 0.9:
                        #print(paquete2)
                        paquetesEliminar.append(paquete2)
                        break
            if len(paquetesEliminar) == N - 1:
                answer = answer + 1
                for n in range(len(paquetesEliminar)):
                    Q[n + 1].remove(paquetesEliminar[n])
                break
                
    print("Case #{}: {}".format(i, answer))
    file2.write("Case #{}: {}\n".format(i, answer))
        
file1.close()
file2.close()
