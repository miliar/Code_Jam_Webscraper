def blanco(clientes):
    for i in range(len(clientes)):
        if(clientes[i]!=0):
            return False
    return True

def dividir(clientes,deep):
    itmp = 0
    value = 0
    newclient = clientes[:]
    if(blanco(newclient)):
        return deep
    for i in range(len(newclient)):
        if(newclient[i]>value):
            value=newclient[i]
            itmp=i
    if(value==1):
        return deep+1
    if(value==9):
        newclient2 = newclient[:]
        tmpvalue = 4
        newclient[itmp] = tmpvalue
        newclient.append(value-tmpvalue)
        if(blanco(newclient)):
            return deep+1
        deep1 = recurrencia(newclient,deep+1)
        tmpvalue = 3
        newclient2[itmp] = tmpvalue
        newclient2.append(value-tmpvalue)
        if(blanco(newclient)):
            return deep+1
        deep2 = recurrencia(newclient2,deep+1)
        return min(deep1,deep2)
    tmpvalue = value//2
    newclient[itmp] = tmpvalue
    newclient.append(value-tmpvalue)
    if(blanco(newclient)):
        return deep+1
    #print("sadf",value,newclient)
    return recurrencia(newclient,deep+1)

def restar(clientes,deep):
    newclient = clientes[:]
    #print("restando con: ",newclient)
    newdeep = deep+0
    if(blanco(newclient)):
        
        return newdeep
    for i in range(len(newclient)):
        tmp = newclient[i]
        if(newclient[i]>=1):
            newclient[i]-=1
    if(blanco(newclient)):
        return newdeep+1
    #print("restado en: ",newclient)
    return recurrencia(newclient,newdeep+1)

def recurrencia(clientes,deep):
    newdeep = deep+0
    if (blanco(clientes)):
        return newdeep
    #print("voy a restar con",clientes)
    deep1 = restar(clientes,newdeep)
    #print("voy a dividir con",clientes)
    deep2 = dividir(clientes,newdeep)
    #print("resultado: restando",deep1," dividiendo", deep2, clientes)
    return min(deep1,deep2)

def main():
    casos = int(input())
    for i in range(casos):
        D = input()
        clientes = [int(x) for x in input().strip().split()]
        print("Case #"+str(i+1)+":",recurrencia(clientes,0))
main()
