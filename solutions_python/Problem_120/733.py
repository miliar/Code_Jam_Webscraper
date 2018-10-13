def cin(str):
    str.strip('\n')
    l = []
    while True:
        pos = str.find(' ')
        if pos == -1:
            number = int(str)
            l.append(number)
            break
        else:
            number = int(str[:pos])
            str = str[pos+1:]
            l.append(number)
    return l        
        

def mainfunction():
    infile = open('input.in','r')
    outfile = open('output.out','w')
    
    Line1 = infile.readline()
    NumCases = cin(Line1)[0]
##    print ('NumCases : ',NumCases)

    for i in range(1,NumCases+1):
            Line2 = infile.readline()
            A = cin(Line2)[0]
##            print ('A :', A)
            B = cin(Line2)[1]
##            print('B : ', B)

            
            
            
            LineOut = 'Case #{0}: \n'.format(i) 
##            outfile.write(LineOut)
##            print(LineOut)
    outfile.close()
    infile.close()

                 
