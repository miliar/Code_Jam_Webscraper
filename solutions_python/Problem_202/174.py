class gridModel:
    modelInserted = ""
    modelAccepted = set()
    
    def __init__(self, modelInserted, modelAccepted):
        self.modelInserted = modelInserted
        self.modelAccepted = modelAccepted

    def getModel(self):
        return self.modelInserted

    def getAccepted(self):
        return self.modelAccepted

    def removeAccepted(self, typeModel):
        if typeModel in self.modelAccepted:
            self.modelAccepted.remove(typeModel)

    def setModel(self, typeModel):
        self.modelInserted = typeModel

class customModels:
    typeModel = ""
    row = 0
    column = 0
    
    def __init__(self, typeModel, row, column):
        self.typeModel = typeModel
        self.row = row
        self.column = column

    def getType(self):
        return self.typeModel

    def getRow(self):
        return self.row

    def getColumn(self):
        return self.column
"""
class iteradorExterno:
    fila = 0
    columna = 0
    deltaFila = 0
    deltaColumna = 0
    acceptedFilas = list()
    acceptedColumnas = list()

    def __init__(self, N):
        self.fila = 0
        self.columna = 0
        self.deltaFila = 0
        self.deltaColumna = 1
        self.acceptedFilas = list(range(N))
        self.acceptedColumnas = list(range(N))

    def changeDeltas(self):
        if self.deltaColumna == 1:
            self.deltaColumna = 0
            self.deltaFila = 1
            self.acceptedFilas.remove(self.fila)
            return False
        elif self.deltaColumna == -1:
            self.deltaColumna = 0
            self.deltaFila = -1
            self.acceptedFilas.remove(self.fila)
            return False
        elif self.deltaFila == 1:
            self.deltaFila = 0
            self.deltaColumna = -1
            self.acceptedColumnas.remove(self.columna)
            return False
        elif self.deltaFila == -1:
            self.deltaFila = 0
            self.deltaColumna = 1
            self.acceptedColumnas.remove(self.columna)
            return True
            

    def moveCoords(self):
        while (not self.fila + self.deltaFila in self.acceptedFilas) or (not self.columna + self.deltaColumna in self.acceptedColumnas):
            caca = self.changeDeltas()
            if (len(self.acceptedColumnas) == 0 and len(self.acceptedFilas) == 0):
                return -1
            if caca:
                return 1

        self.fila = self.fila + self.deltaFila
        self.columna = self.columna + self.deltaColumna
        return 0

    def getCoords(self):
        return self.fila, self.columna
"""

def createGrid(N):
    rows = list()
    for i in range(N):
        columns = list()
        for j in range(N):
            columns.append(gridModel("_", {"o", "+", "x"}))
        rows.append(columns)
    return rows

def clearVerHor(gridModels, N, fila, colu):
    for i in range(N):
        if (i != colu):
            gridModels[fila][i].removeAccepted("o")
            gridModels[fila][i].removeAccepted("x")
    for i in range(N):
        if (i != fila):
            gridModels[i][colu].removeAccepted("o")
            gridModels[i][colu].removeAccepted("x")

def clearDiagonal(gridModels, N, fila, colu):
    suma = fila + colu
    for i in range(N):
        j = suma - i
        if j in range(N):
            if (i, j) != (fila, colu):
                gridModels[i][j].removeAccepted("o")
                gridModels[i][j].removeAccepted("+")

    resta = fila - colu
    for i in range(N):
        j = i - resta
        if j in range(N):
            if (i, j) != (fila, colu):
                gridModels[i][j].removeAccepted("o")
                gridModels[i][j].removeAccepted("+")
        
"""
def replaceOs(gridModels, N, newModels):
    IT = iteradorExterno(N)
    IT2 = iteradorExterno(N)
    while True:
        fila, colu = IT.getCoords() 
        if gridModels[fila][colu].getModel() in ("+", "x"):
            if "o" in gridModels[fila][colu].getAccepted():
                gridModels[fila][colu].setModel("o")
                clearVerHor(gridModels, N, fila, colu)
                clearDiagonal(gridModels, N, fila, colu)
                newModels.append(customModels("o", fila, colu))
        caca = IT.moveCoords()
        if caca == -1:
            break
        elif caca == 1:
            while True:
                fila2, colu2 = IT2.getCoords()
                if gridModels[fila2][colu2].getModel() == "_":
                    if "o" in gridModels[fila2][colu2].getAccepted():
                        gridModels[fila2][colu2].setModel("o")
                        clearVerHor(gridModels, N, fila2, colu2)
                        clearDiagonal(gridModels, N, fila2, colu2)
                        newModels.append(customModels("o", fila2, colu2))
                caca2 = IT2.moveCoords()
                if caca2 == -1 or caca2 == 1:
                    break

def addOs(gridModels, N, newModels):
    IT = iteradorExterno(N)
    while True:
        fila, colu = IT.getCoords()
        if gridModels[fila][colu].getModel() == "_":
            if "o" in gridModels[fila][colu].getAccepted():
                gridModels[fila][colu].setModel("o")
                clearVerHor(gridModels, N, fila, colu)
                clearDiagonal(gridModels, N, fila, colu)
                newModels.append(customModels("o", fila, colu))
        if IT.moveCoords() == -1:
            break
"""
def addPlus(gridModels, N, newModels):
    fila = 0
    for colu in range(N):
        if gridModels[fila][colu].getModel() == "_":
            if "+" in gridModels[fila][colu].getAccepted():
                gridModels[fila][colu].setModel("+")
                clearDiagonal(gridModels, N, fila, colu)
                newModels.append(customModels("+", fila, colu))
        elif gridModels[fila][colu].getModel() == "x":
            if "+" in gridModels[fila][colu].getAccepted():
                gridModels[fila][colu].setModel("o")
                clearDiagonal(gridModels, N, fila, colu)
                clearVerHor(gridModels, N, fila, colu)
                newModels.append(customModels("o", fila, colu))

    fila = N - 1
    for colu in range(1, N - 1):
        if gridModels[fila][colu].getModel() == "_":
            if "+" in gridModels[fila][colu].getAccepted():
                gridModels[fila][colu].setModel("+")
                clearDiagonal(gridModels, N, fila, colu)
                newModels.append(customModels("+", fila, colu))
        elif gridModels[fila][colu].getModel() == "x":
            if "+" in gridModels[fila][colu].getAccepted():
                gridModels[fila][colu].setModel("o")
                clearDiagonal(gridModels, N, fila, colu)
                clearVerHor(gridModels, N, fila, colu)
                newModels.append(customModels("o", fila, colu))
    """
    IT = iteradorExterno(N)
    while True:
        fila, colu = IT.getCoords()
        if gridModels[fila][colu].getModel() == "_":
            if "+" in gridModels[fila][colu].getAccepted():
                gridModels[fila][colu].setModel("+")
                clearDiagonal(gridModels, N, fila, colu)
                newModels.append(customModels("+", fila, colu))
        if IT.moveCoords() == -1:
            break
    """

def addXs(gridModels, N, newModels):
    for colu in range(N):
        existeX = False
        posPlus = None
        for fila in range(N):
            if gridModels[fila][colu].getModel() == "x":
                existeX = True
            elif gridModels[fila][colu].getModel() == "+":
                if "x" in gridModels[fila][colu].getAccepted():
                    posPlus = fila

        if not existeX:
            if posPlus != None:
                gridModels[posPlus][colu].setModel("o")
                clearVerHor(gridModels, N, posPlus, colu)
                clearDiagonal(gridModels, N, posPlus, colu)
                modelo = None
                for model in newModels:
                    if model.getType() == "+" and model.getRow() == posPlus and model.getColumn() == colu:
                        modelo = model
                if modelo != None:
                    newModels.remove(modelo)
                newModels.append(customModels("o", posPlus, colu))
            else:
                for fila in range(N):
                    if gridModels[fila][colu].getModel() == "_":
                        if "x" in gridModels[fila][colu].getAccepted():
                            gridModels[fila][colu].setModel("x")
                            clearVerHor(gridModels, N, fila, colu)
                            newModels.append(customModels("x", fila, colu))
                            break
            
    """
    IT = iteradorExterno(N)
    while True:
        fila, colu = IT.getCoords()
        if gridModels[fila][colu].getModel() == "_":
            if "x" in gridModels[fila][colu].getAccepted():
                gridModels[fila][colu].setModel("x")
                clearVerHor(gridModels, N, fila, colu)
                newModels.append(customModels("x", fila, colu))
        if IT.moveCoords() == -1:
            break
    """

def calculatePoints(gridModels, N):
    result = 0
    for fila in range(N):
        for colu in range(N):
            typeModel = gridModels[fila][colu].getModel()
            if typeModel == "o":
                result = result + 2
            elif typeModel == "+":
                result = result + 1
            elif typeModel == "x":
                result = result + 1
    return result


T = int(input())
#T = 10
for i in range(1, T + 1):
    N, M = [int(s) for s in input().split(" ")]
    #print("Input #{}: {} {}".format(i, N, M))
    totalPoints = 0
    newModels = list()
    gridModels = createGrid(N)
    
    for j in range(M):
        listEntrada = input().split(" ")
        typeModel = listEntrada[0]
        R = int(listEntrada[1])
        C = int(listEntrada[2])
        #print("{} {} {}".format(typeModel, R, C))
        gridModels[R - 1][C - 1].setModel(typeModel)
        if typeModel == "o":
            clearVerHor(gridModels, N, R - 1, C - 1)
            clearDiagonal(gridModels, N, R - 1, C - 1)
        elif typeModel == "+":
            clearDiagonal(gridModels, N, R - 1, C - 1)
        else:
            clearVerHor(gridModels, N, R - 1, C - 1)

    #replaceOs(gridModels, N, newModels)
    #addOs(gridModels, N, newModels)
    addPlus(gridModels, N, newModels)
    addXs(gridModels, N, newModels)

    totalPoints = calculatePoints(gridModels, N)
    
    print("Case #{}: {} {}".format(i, totalPoints, len(newModels)))
    for model in newModels:
        print("{} {} {}".format(model.getType(), model.getRow() + 1, model.getColumn() + 1))  
    """
    for i in range(N):
        for j in range(N):
            print(str(gridModels[i][j].getModel()).ljust(1), end = " ")
        print("")
    """
