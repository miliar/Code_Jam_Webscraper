'''
Created on 07/05/2010

@author: jpsantos
'''
def make_mask(n):
    ret = 1
    for j in range(n-1):
        ret = ret << 1
        ret = ret + 1
    return ret


filename = raw_input('Input file:')
infile = open(filename, 'r')
outfile = open("%s.%s"%(filename,'out'), 'w')

tests = int(infile.readline())

for i in range(tests):
    line = infile.readline()
    splitValues = line.split()
    n = int(splitValues[0])
    k = int(splitValues[1])
    
    mask = make_mask(n)
    
    aux = 0
    for ii in range(k):
        aux = aux + 1
    
    result = ((aux & mask) ^ mask)
    
    #print bin(aux)
    if not (result):
        outfile.write('Case #%d: %s\n' % (i+1,'ON'))
    else:
        outfile.write('Case #%d: %s\n' % (i+1,'OFF'))
    
        

    


if __name__ == '__main__':
    pass