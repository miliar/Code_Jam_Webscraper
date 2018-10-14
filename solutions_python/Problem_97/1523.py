
#Small dataset. [0001, 1000]
#Large dataset. [0000001, 2000000]

from math import log10, trunc

def toIntList(slist):
    tmplst = []
    for item in slist:
        tmplst.append(int(item))
    return tmplst

def recycledNumbers(a,b):
    recycledPairs = []
    #for each number between a and b
    for i in range(a,b+1):
        s = str(i)
        for ctr in range(1, len(s)+1):
            newNum = int(s[-ctr:]+s[:len(s)-ctr])
            #print(i, newNum)
            if (\
                (newNum >  i) and \
                (newNum <= b) and \
                not((i,newNum) in recycledPairs)\
                ):
                recycledPairs.append( (i,newNum) )
    #print (recycledPairs)
    return(len(recycledPairs))

def solve_func(infile, outfile):
    #read the number of cases
    cases = int(str(infile.readline()[:-1], 'utf8'))
    #for each case
    for i in range(cases):
        #process the string
        line = toIntList(str(infile.readline()[:-1], 'utf8').split(' '))
        msg = 'Case #%d: %d\n' % (i+1, recycledNumbers(line[0], line[1]))
        outfile.write(bytes(msg, 'utf8'))


if __name__ == '__main__':
    infile  = open('C-small-attempt0.in', 'rb')
    outfile = open('out', 'wb')
    try:
        solve_func(infile, outfile)
    finally:
        infile.close()
        outfile.close()
