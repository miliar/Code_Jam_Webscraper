fileName = input("File Name: ")
if fileName == "":
    fileName = "A-large.in"
file1 = open(fileName)
file2 = open("sol_" + fileName, "w")

def contagiarVertical(matrix, fila, columna):
    if fila - 1 >= 0:
        if matrix[fila - 1][columna] == "?":
            matrix[fila - 1][columna] = matrix[fila][columna]
            contagiarVertical(matrix, fila - 1, columna)
    if fila + 1 < len(matrix):
        if matrix[fila + 1][columna] == "?":
            matrix[fila + 1][columna] = matrix[fila][columna]
            contagiarVertical(matrix, fila + 1, columna)

def contagiarHorizontal(matrix, fila, columna):
    if columna - 1 >= 0:
        if matrix[fila][columna - 1] == "?":
            matrix[fila][columna - 1] = matrix[fila][columna]
            contagiarHorizontal(matrix, fila, columna - 1)
    if columna + 1 < len(matrix[0]):
        if matrix[fila][columna + 1] == "?":
            matrix[fila][columna + 1] = matrix[fila][columna]
            contagiarHorizontal(matrix, fila, columna + 1)
        
    
T = int(file1.readline())
for i in range(1, T + 1):
    R, C = [int(s) for s in file1.readline().split(" ")]
    matrix = list()
    for r in range(R):
        matrix.append(list(file1.readline().strip()))

    for fila in range(R):
        for columna in range(C):
            if matrix[fila][columna] != "?":
                contagiarVertical(matrix, fila, columna)
    for fila in range(R):
        for columna in range(C):
            if matrix[fila][columna] != "?":
                contagiarHorizontal(matrix, fila, columna)

    print("Case #{}:".format(i))
    for fila in range(R):
        for columna in range(C):
            print(matrix[fila][columna].ljust(1), end = "")
        print("")
        
    file2.write("Case #{}:\n".format(i))
    for fila in range(R):
        for columna in range(C):
            file2.write(matrix[fila][columna])
        file2.write("\n")
        
file1.close()
file2.close()
