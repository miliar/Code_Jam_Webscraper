i = 0
IN = open('ToungeIn.txt','r')
OUT = open('ToungeOut.txt','w')
for line in IN:
    i = i + 1
    if (i == 1):
        total_cases = int(line)
    else:
        answer = ""
        for char in line:
            if (char == ' '):
                answer = answer + ' '
            elif (char == 'a'):
                answer = answer + 'y'
            elif (char == 'b'):
                answer = answer + 'h'
            elif (char == 'c'):
                answer = answer + 'e'
            elif (char == 'd'):
                answer = answer + 's'
            elif (char == 'e'):
                answer = answer + 'o'
            elif (char == 'f'):
                answer = answer + 'c'
            elif (char == 'g'):
                answer = answer + 'v'
            elif (char == 'h'):
                answer = answer + 'x'
            elif (char == 'i'):
                answer = answer + 'd'
            elif (char == 'j'):
                answer = answer + 'u'
            elif (char == 'k'):
                answer = answer + 'i'
            elif (char == 'l'):
                answer = answer + 'g'
            elif (char == 'm'):
                answer = answer + 'l'
            elif (char == 'n'):
                answer = answer + 'b'
            elif (char == 'o'):
                answer = answer + 'k'
            elif (char == 'p'):
                answer = answer + 'r'
            elif (char == 'q'):
                answer = answer + 'z'
            elif (char == 'r'):
                answer = answer + 't'
            elif (char == 's'):
                answer = answer + 'n'
            elif (char == 't'):
                answer = answer + 'w'
            elif (char == 'u'):
                answer = answer + 'j'
            elif (char == 'v'):
                answer = answer + 'p'
            elif (char == 'w'):
                answer = answer + 'f'
            elif (char == 'x'):
                answer = answer + 'm'
            elif (char == 'y'):
                answer = answer + 'a'
            elif (char == 'z'):
                answer = answer + 'q'
        print "Case #{0}: {1}\n".format(i+1,answer)
        OUT.write("Case #{0}: {1}\n".format(i-1,answer))
OUT.close()


        
