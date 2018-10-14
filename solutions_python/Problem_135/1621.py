import sys

i = 0
j = 0
caso = 0
p1 = ''
p2 = ''
mat1 = []
mat2 = []

def comprueba(line1,line2):
    piv = 0
    valor = ''
    for val in line1:
        for val1 in line2:
            if val == val1:
                piv = piv + 1
                valor = val
    if piv == 1:
        return valor
    if piv == 0:
        return 'Volunteer cheated!'
    if piv > 1:
        return 'Bad magician!'

for line in sys.stdin:
    i = i + 1
    if i != 1:
        j = j + 1
        if j == 1:
            p1 = line.strip()
        if j >= 2 and j <= 5:
            mat1.append((line.strip()).split())
        if j == 6:
            p2 = line.strip()
        if j >= 7 and j <= 10:
            mat2.append((line.strip()).split())
        if j == 10:
            caso = caso + 1
            print (("Case #%i: %s")% (caso,comprueba(mat1[int(p1)-1], mat2[int(p2)-1])))
            mat1=[]
            mat2=[]
            j = 0