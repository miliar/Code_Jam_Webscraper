import sys
#sys.stdout = open("salida.out", "w")

def moverazul():
    global blue
    if botsblue:
        lugar = botsblue[0][1]
        if blue < lugar:
            blue += 1
        elif blue > lugar:
            blue -= 1
        
def moverorange():
    global orange
    if botsorange:
        lugar = botsorange[0][1]
        if orange < lugar:
            orange += 1
        elif orange > lugar:
            orange -= 1
            
handle = open("entrada.in")

casos = int(handle.readline())

for caso in xrange(1, casos + 1):
    linea = handle.readline()
    spl = linea.split()
    cantbotones = int(spl[0])
    botones = spl[1:]
    bots = []
    for i in xrange(cantbotones):
        bots.append((botones[2 * i], int(botones[2 * i + 1])))
    botsorange = [bot for bot in bots if bot[0] == 'O']
    botsblue = [bot for bot in bots if bot[0] == 'B']
    tiempo = 0
    orange = 1
    blue = 1    
    while bots:
        primerboton = bots[0]
        primerrobot = primerboton[0]
        primerlugar = primerboton[1]
        if primerrobot == 'O':
            if orange == primerlugar:
                bots = bots[1:]
                botsorange = botsorange[1:]
            else:
                moverorange()
            moverazul()
        else:
            if blue == primerlugar:
                bots = bots[1:]
                botsblue = botsblue[1:]
            else:
                moverazul()
            moverorange()
        tiempo += 1
    print "Case #%s: %s" % (caso, tiempo)
        