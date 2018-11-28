def areRecycled(number1, number2):
    recycled = False
    numero1 = number1
    for i in range(len(number2)):
        numero1.insert(0,numero1.pop())
        if numero1 == number2:
            return True
    return False

    

archi = open("C-small-attempt2.in","r")
cant = open("output.dat","w")
cases = int(archi.readline().split()[0])
for i in range(cases):
    cont = 0
    label = "Case #" + str(i+1) + ": "    
    numeros = archi.readline().replace('\n','').split(" ")
    limInferior = int(numeros[0])
    limSuperior = int(numeros[1])
    j=limInferior
    while j < limSuperior:
    	k=j+1;
        while k<= limSuperior:
            if areRecycled(list(str(k)),list(str(j))):
                cont = cont + 1
            k = k + 1
        j = j + 1
    label = label + str(cont) + '\n'
    cant.writelines(label)



    	

