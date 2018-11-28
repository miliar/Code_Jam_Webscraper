'''
Created on 08/05/2011

@author: Admin
'''

def read(fIn):
    line = fIn.readline().strip()
#    print "READ: {0}".format(line)
    return line

def doFormat(picture, cols):
    output = ""
    for i,c in enumerate(picture):
        output = output + c
        if (i+1) % cols == 0:
            output = output + "\n"
    return output

if __name__ == '__main__':
    fInput = open('input.txt')
    fOutput = open('output.txt', 'w')
    
    numCases = int(fInput.readline().strip());
    for num in range(1, numCases + 1):
        print "Running test {0}/{1}".format(num, numCases)
        firstLine = read(fInput);
        
        rows,cols= firstLine.split()
        rows = int(rows)
        cols = int(cols)

        picture = ""
        for cr in range(0, rows):
            picture = picture + read(fInput)
            
        picture = list(picture)
#        print "Pic is {}".format(picture)
        
        impossible = False
        
        for i in range(0, rows * cols):
            c = picture[i]
            x = i % (rows+1)
            y = i / cols
            
            if c == '#':
                if i+cols+1 >= len(picture):
                    print "No space - Probably impossible!"
                    impossible = True
                else:
                    c2 = picture[i+1]
                    c3 = picture[i+cols]
                    c4 = picture[i+cols+1]
                    print x,y, c, c2, c3, c4
                    if c2 == '#' and c3 =='#' and c4 == '#':
                        picture[i] = '/'
                        picture[i+1] = '\\'
                        picture[i+cols] = '\\'
                        picture[i+cols+1] = '/'
#                        print "Modified - curr is {}".format(doFormat(picture))
                    else:
                        print "No room for block - Probably impossible!"
                        impossible = True
            
            if impossible:
                break
        
        result = picture[:]
        
        
        output = ""
        if impossible:
            output = "Impossible\n"
        else:
            output = doFormat(picture, cols)
            
        toWrite = "Case #{0}:\n{1}".format(num, output)
        print toWrite
        fOutput.write(toWrite)
        
    print "All done!"
