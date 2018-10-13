import re

def execute(name):
    file = open(name, 'a')
    file.write(" ")
    file.close()
    file = open(name, 'r')
    n = eval(file.readline())
    i = 1
    out = open('out.txt', 'w')
    while (i <= n):
        z = file.readline()
        print(z)
        size = eval(re.findall(r'\d+', z)[0]) #tamanho da espatula
        print(size)
        z = z[:-(numero_digitos(size)+2)]
        print(z)
        y = len(z) - 1 #numero elementos na linha
        j = 0
        res = 0
        while (j < y):
            printed = 0
            if (z[j] == '+'):
                j += 1
            else:
                z = list(z)
                if((j + size) <= y):
                    res += 1
                    z[j] = '+'
                    g = 1
                    while (g < size):
                        if (z[j + g] == '+'):
                            z[j + g] = '-'
                            g += 1
                        else:
                            z[j + g] = '+'
                            g += 1
                else:
                    printed = 1
                    out.write ("Case #" + str(i) + ": IMPOSSIBLE" + "\n")
                    j = y
                j += 1
        if(printed == 0):
            out.write ("Case #" + str(i) + ": " + str(res) + "\n")
        i+=1
    out.close()
    file.close()

def numero_digitos (x):
    res = 0
    while x != 0:
        res += 1
        x = x // 10
    return res