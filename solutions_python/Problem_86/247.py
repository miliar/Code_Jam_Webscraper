'''
Created on 08/05/2011

@author: Admin
'''

def read(fIn):
    line = fIn.readline().strip()
    print "READ: {0}".format(line)
    return line

if __name__ == '__main__':
    fInput = open('input.txt')
    fOutput = open('output.txt', 'w')
    
    numCases = int(fInput.readline().strip());
    for num in range(1, numCases + 1):
        print "Running test {0}/{1}".format(num, numCases)
        params = read(fInput).split();
        
        Nplayers = int(params[0])
        lowest = int(params[1])
        highest = int(params[2])
        
        notes = [int(note) for note in read(fInput).split()];
        
        result = -1
        
        for possible in range(lowest, highest+1):
            badNote = False
            for note in notes:
                if note % possible != 0 and possible % note != 0:
                    badNote = True
                    break
                
            if (not badNote):
                result = possible
                break;
        
        output = ""
        if (result == -1):
            output = "NO"
        else:
            output = result 
            
        toWrite = "Case #{0}: {1}\n".format(num, output)
        print toWrite
        fOutput.write(toWrite)
        
    print "All done!"
