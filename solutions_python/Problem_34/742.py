# Alien Language 

entrada = raw_input()
entrada = entrada.split()
l = int (entrada[0])
d = int (entrada[1])
n = int (entrada[2])
dic = []

def divide (string):
    n = []
    aux = ""
    achou = 0
    for i in range(len(string)):
        if string[i] == "(":
            achou = 1
        if achou == 1:
            aux = aux + string[i]
        if achou == 0:
            n.append(string[i])
        if string[i] == ")" :
            achou = 0
            n.append(aux)
            aux = ""
            
    return n


for i in range(d):             
    word = raw_input()
    dic.append(word)
    

case = 0
for i in range(n):
    case += 1
    cont = len(dic)
    w = raw_input()
    lw = divide(w)
    for palavra in dic:
        for j in range(l):
            if palavra[j] not in lw[j]:
                cont -= 1
                break
                
        

    print "Case #" + str(case) +": " + str(cont)
