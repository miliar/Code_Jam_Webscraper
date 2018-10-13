class cake:
    _lista = []
    _fatias = {}
    _altura = 0
    _largura = 0
    def __init__(self, altura, largura):
        self._altura = altura
        self._largura = largura
        for i in range(altura):
            linha = []
            for j in range(largura):
                linha = linha + ["?"]
            self._lista = self._lista + [linha]
    def setLetra(self, letra, linha, coluna):
        self._lista[linha][coluna] = letra
        self._fatias[letra] = (linha, coluna, linha, coluna)
        
    def show(self):
        print()
        for i in self._lista:
            string = ""
            for j in i:
                string = string + j
            print(string)
        return
        
    def maxExpand(self, letra):
        self.maxTop(letra)
        self.maxRight(letra)
        self.maxBot(letra)
        self.maxLeft(letra)
        
    def solve(self):
        for letra in list(self._fatias):
            self.maxExpand(letra)
               
    def isDone(self):
        for i in self._lista:
            for j in i:
                if j== "?":
                    return False
        return True
        
    def soLetra(self, letra, l1, c1, l2, c2):
        for a in range((l2-l1)+1):
            i = a+l1
            for b in range((c2-c1)+1):
                j = b+c1
                if not self._lista[i][j] in ("?", letra):
                    return False
        return True
    
    def pinta(self, letra, l1, c1, l2, c2):
        for a in range((l2-l1)+1):
            i = a+l1
            for b in range((c2-c1)+1):
                j = b+c1
                self._lista[i][j] = letra
        return
    
    def maxTop(self, letra):
        if(self._fatias[letra][0] == 0):
            print(letra, "esta no maximo para cima")
            return
        else:
            if self.soLetra(letra, self._fatias[letra][0]-1, self._fatias[letra][1], self._fatias[letra][2], self._fatias[letra][3]):
                self._fatias[letra] = (self._fatias[letra][0]-1, self._fatias[letra][1], self._fatias[letra][2], self._fatias[letra][3])
                self.pinta(letra, self._fatias[letra][0], self._fatias[letra][1], self._fatias[letra][2], self._fatias[letra][3])
                return self.maxTop(letra)
            else:
                print(letra, "esta no maximo para cima")
                return
            
    def maxRight(self, letra):
        if(self._fatias[letra][3] == self._largura-1):
            print(letra, "esta no maximo para a direita")
            return
        else:
            if self.soLetra(letra, self._fatias[letra][0], self._fatias[letra][1], self._fatias[letra][2], self._fatias[letra][3]+1):
                self._fatias[letra] = (self._fatias[letra][0], self._fatias[letra][1], self._fatias[letra][2], self._fatias[letra][3]+1)
                self.pinta(letra, self._fatias[letra][0], self._fatias[letra][1], self._fatias[letra][2], self._fatias[letra][3])
                return self.maxRight(letra)
            else:
                print(letra, "esta no maximo para a direita")
                return
            
    def maxBot(self, letra):
        if(self._fatias[letra][2] == self._altura-1):
            print(letra, "esta no maximo para baixo")
            return
        else:
            if self.soLetra(letra, self._fatias[letra][0], self._fatias[letra][1], self._fatias[letra][2]+1, self._fatias[letra][3]):
                self._fatias[letra] = (self._fatias[letra][0], self._fatias[letra][1], self._fatias[letra][2]+1, self._fatias[letra][3])
                self.pinta(letra, self._fatias[letra][0], self._fatias[letra][1], self._fatias[letra][2], self._fatias[letra][3])
                return self.maxBot(letra)
            else:
                print(letra, "esta no maximo para baixo")
                return
        
    def maxLeft(self, letra):
        if(self._fatias[letra][1] == 0):
            print(letra, "esta no maximo para a exquerda")
            return
        else:
            if self.soLetra(letra, self._fatias[letra][0], self._fatias[letra][1]-1, self._fatias[letra][2], self._fatias[letra][3]):
                self._fatias[letra] = (self._fatias[letra][0], self._fatias[letra][1]-1, self._fatias[letra][2], self._fatias[letra][3])
                self.pinta(letra, self._fatias[letra][0], self._fatias[letra][1], self._fatias[letra][2], self._fatias[letra][3])
                return self.maxLeft(letra)
            else:
                print(letra, "esta no maximo para a exquerda")
                return
                
def openFile(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()  
    return lines

def do(filename):
    lines = openFile(filename)
    sol = solvelines(lines)
    file = open("solution" + filename, "w")
    file.write(sol)
    file.close
    
def solvelines(lines):
    count = eval(lines[0])
    lines = lines[1:]
    outtxt = ""
    for i in range(count):
        sizes = lines[0].split()
        lines = lines[1:]
        cak = cake(eval(sizes[0]), eval(sizes[1]))
        cak._fatias = {}
        print(cak._fatias)
        for j in range(eval(sizes[0])):
            line = lines[0]
            lines = lines[1:]
            for k in range(eval(sizes[1])):
                if line[k] != "?":
                    cak.setLetra( line[k], j, k)
        print(cak._altura, cak._largura)
        print(cak._fatias)
        cak.show()
        cak.solve()
        cak.show()
        print(cak._fatias)
        outtxt = outtxt + "Case #" + str(i+1) + ":\n"
        for j in cak._lista:
            for k in j:
                outtxt = outtxt + k
            outtxt = outtxt + "\n"
    return outtxt