kb = []
output = open('outputgooglese.in', 'w')

def read(path):
    f = open(path)
    x = 1
    f.readline()
    for line in f:
        new = 'Case #' + str(x) + ': '
        index = 0
        while index < len(line):
            letter = line[index]
            new = new + swap(letter)
            index = index + 1
        new = new + "\n"
        output.write(new)
        x = x+1

def swap(letter):
    if(letter == 'a'):
        return 'y'
    elif(letter == 'b'):
        return 'h'
    elif(letter == 'c'):
        return 'e'
    elif(letter == 'd'):
        return 's'
    elif(letter == 'e'):
        return 'o'
    elif(letter == 'f'):
        return 'c'
    elif(letter == 'g'):
        return 'v'
    elif(letter == 'h'):
        return 'x'
    elif(letter == 'i'):
        return 'd'
    elif(letter == 'j'):
        return 'u'
    elif(letter == 'k'):
        return 'i'
    elif(letter == 'l'):
        return 'g'
    elif(letter == 'm'):
        return 'l'
    elif(letter == 'n'):
        return 'b'
    elif(letter == 'o'):
        return 'k'
    elif(letter == 'p'):
        return 'r'
    elif(letter == 'q'):
        return 'z'
    elif(letter == 'r'):
        return 't'
    elif(letter == 's'):
        return 'n'
    elif(letter == 't'):
        return 'w'
    elif(letter == 'u'):
        return 'j'
    elif(letter == 'v'):
        return 'p'
    elif(letter == 'w'):
        return 'f'
    elif(letter == 'x'):
        return 'm'
    elif(letter == 'y'):
        return 'a'
    elif(letter == 'z'):
        return 'q'
    else:
        return " "

def close():
    output.close()
