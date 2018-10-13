import string
finput = open('A-small-attempt4.in','r')
cases = int(finput.readline())
foutput = open('output','w')
for case in range(cases):
    inputstr = finput.readline()
    string.lower(inputstr)
    n_input = len(inputstr)
    output = ''
    for index in range(n_input):
        if inputstr[index] == 'a':
            output += 'y'
        elif inputstr[index] == 'b':
            output += 'h'
        elif inputstr[index] == 'c':
            output += 'e'
        elif inputstr[index] == 'd':
            output += 's'
        elif inputstr[index] == 'e':
            output += 'o'
        elif inputstr[index] == 'f':
            output += 'c'
        elif inputstr[index] == 'g':
            output += 'v'
        elif inputstr[index] == 'h':
            output += "x"
        elif inputstr[index] == 'i':
            output += 'd'
        elif inputstr[index] == 'j':
            output += 'u'
        elif inputstr[index] == 'k':
            output += 'i'
        elif inputstr[index] == 'l':
            output += 'g'
        elif inputstr[index] == 'm':
            output += 'l'
        elif inputstr[index] == 'n':
            output += 'b'
        elif inputstr[index] == 'o':
            output += 'k'
        elif inputstr[index] == 'p':
            output += 'r'
        elif inputstr[index] == 'q':
            output += 'z'
        elif inputstr[index] == 'r':
            output += 't'
        elif inputstr[index] == 's':
            output += 'n'
        elif inputstr[index] == 't':
            output += 'w'
        elif inputstr[index] == 'u':
            output += 'j'
        elif inputstr[index] == 'v':
            output += 'p'
        elif inputstr[index] == 'w':
            output += 'f'
        elif inputstr[index] == 'x':
            output += 'm'
        elif inputstr[index] == 'y':
            output += 'a'
        elif inputstr[index] == 'z':
            output += 'q'
        else :
            output += inputstr[index]
                                       
    beautyoutput = 'Case #'+str(case+1)+': '+output+'\n'
    foutput.write(beautyoutput)
foutput.close()
