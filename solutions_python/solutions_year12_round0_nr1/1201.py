import math

def main():
    inFile = open('c:/jam/2012/A-small-attempt0.in')
    
    c = int(inFile.readline())
    print c

    r = []
    #dict = {' ': ' ', 'a': 'y', 'c': 'f', 'b': 'n', 'e': 'c', 'd': 'i', 'g': 'l', 'f': 'w', 'i': 'k', 'h': 'b', 'k': 'o', 'j': 'u', 'm': 'x', 'l': 'm', 'o': 'e', 'n': 's', 'p': 'v', 's': 'd', 'r': 'p', 'u': 'j', 't': 'r', 'w': 't', 'v': 'g', 'y': 'a', 'x': 'h'}
    dict = {' ': ' ', 'z':'q', 'q':'z', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}
    #dict = {}
    
    ro = ['our language is impossible to understand', 'there are twenty six factorial possibilities', 'so it is okay if you want to just give up']
    
    for i in range(0, c):
        line = inFile.readline()

        res = ''
        for j in range(0, len(line)-1):
            res += dict[line[j]]
            #dict[line[j]] = ro[i][j]
            
        r.append(res)

    outFile = open('c:/jam/2012/A-small-attempt0.out', 'w')
    for i in range(0, c):
        outFile.write('Case #%d: %s\n' % ((i+1), r[i]))
    outFile.close

if __name__ == '__main__':
    main()

