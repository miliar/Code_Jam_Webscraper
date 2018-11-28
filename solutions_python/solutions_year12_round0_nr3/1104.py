'''
Created on Apr 13, 2012

@author: Shan
'''


def get_combs(num):
    numstr = str(num)
    numstrlist = list(numstr)
    nlen = len(numstrlist)
    
    combs = []
    
    count=0
    shifter = 0
    currcomb = ''
    while count < nlen*nlen:
        if count % nlen == 0:
            currcomb = ''
        currcomb += numstrlist[(count + shifter) % nlen]
        if count % nlen == nlen -1:
            if not currcomb in combs:
                combs.append(currcomb)
            shifter += 1
        count +=1
    return combs
    
        

def count_recycles(numa, numb):
    numa = int(numa)
    numb = int(numb)
    posscount = 0
    count = numa
    while count <= numb:
        combos = get_combs(count)
        for c in combos:
            cint = int(c)
            if cint > count and cint <= numb:
                posscount +=1
        count +=1
    
    return str(posscount)

f = open('input.txt', 'r')
lines = f.readlines()

count = int(lines[0])

counter = 1
while counter <= count:
    line = lines[counter]
    line = line.rstrip('\n')
    linesplit = line.split(' ')
    
    print "Case #" + str(counter) + ": " + count_recycles(linesplit[0], linesplit[1])
    counter += 1

f.close()
