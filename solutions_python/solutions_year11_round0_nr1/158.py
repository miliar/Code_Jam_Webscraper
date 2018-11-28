'''
@author: Peratham
'''

INPUTFILE = 'A-large.in'
OUTPUTFILE = 'A-large.out'

def readFile():
    file = open(INPUTFILE, 'r')
    text = file.readline()
    tmp = text.split()
    P = tmp[0]
    
    param = []
    param.append(P)
    input = []
    
    num_button = []
    text = file.readlines()
    for line in text:
        tmp = line.split()
        num_button.append(tmp[0])
        input.append(tmp[1:])
    param.append(num_button)
    
    file.close()
    del file
    return [param, input]
    
def solve(param, input):
    ans = []
    
    for iput in input:
        aOsec = 0
        aBsec = 0
        sec = 0
        Osec = 0
        Bsec = 0
        Opos = 1
        Bpos = 1
        r = -1
        Lastmove = None
        for i in iput:
            if i == 'O':
                r = 0
            elif i == 'B':
                r = 1
            elif r == 0:
                Odes = int(i)
                Osec = abs(Odes - Opos) 
                Opos = Odes
                if Lastmove == 'B':
                    if aBsec > Osec:
                        Osec = 0
                    else:
                        Osec -= aBsec
                    aBsec = 0
                aOsec += (Osec + 1)
                sec += (Osec + 1)
                Lastmove = 'O'
            elif r == 1:
                Bdes = int(i)
                Bsec = abs(Bdes - Bpos) 
                Bpos = Bdes
                if Lastmove == 'O':
                    if aOsec > Bsec:
                        Bsec = 0
                    else:
                        Bsec -= aOsec
                    aOsec = 0
                aBsec += (Bsec + 1) 
                sec += (Bsec + 1)
                Lastmove = 'B'
        ans.append(sec)
    return ans

def writeFile(ans):
    file = open(OUTPUTFILE, 'w')
    file.write("Case #1: %d\n" % ans[0])
    file.close()
    
    file = open(OUTPUTFILE, 'a')
    for i in xrange(len(ans) - 1):
        file.write("Case #%d: %d\n" % ((i + 2), ans[(i + 1)]))
        
    file.close()

def main():
    [param, input] = readFile()
    ans = solve(param, input)
    writeFile(ans)

if __name__ == '__main__':
    main()
