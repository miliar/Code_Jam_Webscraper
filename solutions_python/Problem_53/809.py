from itertools import count

def readFile(fil):
    inFile=open(fil)
    outFile=open('output1.txt', 'w')
    inFile.readline()
    for line, lineNumber in zip(inFile.xreadlines(), count()):
        n,k=line.split()
        n=int(n)
        k=int(k)
        outFile.write('Case #%d: %s\n'%(lineNumber+1,
                                        'ON' if chk(n, k) else 'OFF'))

def chk(n, k):
    if not n: return False
    b=bin(k)[2:]
    return len(b)>=n and (not '0' in b[-n:])
    
if __name__ == '__main__':
    from sys import argv
    readFile(argv[1])
