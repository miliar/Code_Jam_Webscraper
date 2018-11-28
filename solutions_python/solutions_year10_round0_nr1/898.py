from math import pow
import os, sys

def snapper(N, K):
    if (K+1) % (2*pow(2, N-1)) == 0:
        return True
    else:
        return False



def fileIO(inFile):
    IN = open(inFile, 'r')
    OUT = open(os.path.join(os.path.split(inFile)[0], os.path.split(inFile)[1][:-3]+'.out'), 'w')
    l = IN.readline()
    i = 0
    while l:
        ls = l[:-1].split(' ')
        if len(ls) == 1:
            pass
        elif snapper(int(ls[0]), int(ls[1])) == True:
            OUT.write('Case #' + str(i) +': ON\n')
        else:
            OUT.write('Case #' + str(i) +': OFF\n')
        i += 1
        l = IN.readline()

if __name__ == '__main__':
    fileIO(sys.argv[1]) #Assumming I know where I put the file
