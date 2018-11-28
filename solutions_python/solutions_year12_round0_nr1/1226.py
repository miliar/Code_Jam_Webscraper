def goggler(myString):
    if(myString == 'y'): myString = myString.replace('y','a')
    elif(myString == 'n'): myString = myString.replace('n','b')
    elif(myString == 'f'): myString = myString.replace('f','c')
    elif(myString == 'i'): myString = myString.replace('i','d')
    elif(myString == 'c'): myString = myString.replace('c','e')
    elif(myString == 'w'): myString = myString.replace('w','f')
    elif(myString == 'l'): myString = myString.replace('l','g')
    elif(myString == 'b'): myString = myString.replace('b','h')
    elif(myString == 'k'): myString = myString.replace('k','i')
    elif(myString == 'u'): myString = myString.replace('u','j')
    elif(myString == 'o'): myString = myString.replace('o','k')
    elif(myString == 'm'): myString = myString.replace('m','l')
    elif(myString == 'x'): myString = myString.replace('x','m')
    elif(myString == 's'): myString = myString.replace('s','n')
    elif(myString == 'e'): myString = myString.replace('e','o')
    elif(myString == 'v'): myString = myString.replace('v','p')
    elif(myString == 'z'): myString = myString.replace('z','q')
    elif(myString == 'p'): myString = myString.replace('p','r')
    elif(myString == 'd'): myString = myString.replace('d','s')
    elif(myString == 'r'): myString = myString.replace('r','t')
    elif(myString == 'j'): myString = myString.replace('j','u')
    elif(myString == 'g'): myString = myString.replace('g','v')
    elif(myString == 't'): myString = myString.replace('t','w')
    elif(myString == 'h'): myString = myString.replace('h','x')
    elif(myString == 'a'): myString = myString.replace('a','y')
    elif(myString == 'q'): myString = myString.replace('q','z')
    return myString

fob = open('c:/test/a.txt','r')
n = fob.readline()
n = int(n)
j = 1
while j <= n:
    line = fob.readline()
    line = list(line)
    i = 0
    while i < len(line) :
        line[i] = goggler(line[i])
        i += 1
    line = ''.join(line)
    print 'Case #'+`j`+': '+line
    j += 1


    
