from tkinter import filedialog
from tkinter import *

root = Tk()

def decode(message):
    output = []
    for i in range(0, len(message)):
        if message[i] == ' ':
            output.append(' ')
        elif message[i] == 'y':
            output.append('a')
        elif message[i] == 'n':
            output.append('b')
        elif message[i] == 'f':
            output.append('c')
        elif message[i] == 'i':
            output.append('d')
        elif message[i] == 'c':
            output.append('e')
        elif message[i] == 'w':
            output.append('f')
        elif message[i] == 'l':
            output.append('g')
        elif message[i] == 'b':
            output.append('h')
        elif message[i] == 'k':
            output.append('i')
        elif message[i] == 'u':
            output.append('j')
        elif message[i] == 'o':
            output.append('k')
        elif message[i] == 'm':
            output.append('l')
        elif message[i] == 'x':
            output.append('m')
        elif message[i] == 's':
            output.append('n')
        elif message[i] == 'e':
            output.append('o')
        elif message[i] == 'v':
            output.append('p')
        elif message[i] == 'z':
            output.append('q')
        elif message[i] == 'p':
            output.append('r')
        elif message[i] == 'd':
            output.append('s')
        elif message[i] == 'r':
            output.append('t')
        elif message[i] == 'j':
            output.append('u')
        elif message[i] == 'g':
            output.append('v')
        elif message[i] == 't':
            output.append('w')
        elif message[i] == 'h':
            output.append('x')
        elif message[i] == 'a':
            output.append('y')
        elif message[i] == 'q':
            output.append('z')
    newmessage = ''.join(output)
    return newmessage

infile = filedialog.askopenfilename(parent = root, title = 'Open File')
infile = open(infile, 'r')
outfile = open('A-small-attemptout.txt', 'w')
tmp =infile.readline()
cases = eval(tmp)



for j in range(1, cases + 1):
    tmp = infile.readline()
    output = "Case #" + str(j) + ": " + decode(tmp) + "\n"
    outfile.write(str(output))

infile.close()
outfile.close()

root.quit()
root.destroy()
