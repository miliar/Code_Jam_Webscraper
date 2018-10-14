inpfile = open('C:/Users/Dane/Desktop/CJ/A-small-attempt0 (1).in','r')

def compare( a, b):
    return a == b

def countdiflet(a):
   
    lista = []
    for x in a:
        if x not in lista or  x != lista[len(lista)-1]:
            lista += [x]
    return lista

def diff(a,b):
    if a>b:
        return a-b
    elif b>a:
        return b-a
    else:
        return 0

    
def getcount(a):
    lista = countdiflet(a)
    countlist = []
    temp = 0
     
    for i in lista:
        count = 0
        for y in range(temp, len(a)):
            
            if (i == a[y]):
                count += 1

            elif i!= a[y]:
                countlist += [count]
                temp = y
                break;
            if y == (len(a) -1):
                countlist += [count]
    return countlist

def numcount(a,b):
    lista = getcount(a)
    listb = getcount(b)
    num = 0
    for x in range(0, len(lista)):
        num += diff(lista[x], listb[x])
    return num
        

    
def ispos( a, b):
    return (countdiflet(a) == countdiflet(b))

def main():

    wordsl = []
    loop = int(inpfile.readline())

    for i in range(0,loop):
        wordsl= []
        y = int(inpfile.readline())

        for j in range(0,y):
            wordsl += [inpfile.readline()]

        if ispos(wordsl[0], wordsl[1]):
            with  open('C:/Users/Dane/Desktop/CJ/output1b1.txt','a') as out1:
                out1.write('Case #%d: %d' % (i+1, numcount(wordsl[0], wordsl[1])))
                out1.write('\n')
        else:
            with  open('C:/Users/Dane/Desktop/CJ/output1b1.txt','a') as out1:
                out1.write('Case #%d: %s' % (i+1, "Fegla Won"))
                out1.write('\n')

main()
