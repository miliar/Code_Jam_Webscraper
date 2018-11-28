'''
Created on Apr 13, 2012

@author: Shan
'''



def get_max_num(numgooglers, numsurps, minscore, scores):
    
    neededwsurp = 0
    if int(minscore) != 0:
        neededwsurp = (3 * int(minscore)) - 4
        if neededwsurp < 1:
            neededwsurp = 1
    
    needednosurp = 0
    if int(minscore) != 0:
        needednosurp = (3 * int(minscore)) - 2
        if needednosurp < 1:
            needednosurp = 1
    
    
    surpsused = 0
    count = 0
    for s in scores:
        s = int(s)
        if s >= needednosurp:
            count += 1
        elif s >= neededwsurp and surpsused < int(numsurps):
            count += 1
            surpsused +=1
    
    return str(count)

f = open('input.txt', 'r')
lines = f.readlines()

count = int(lines[0])

counter = 1
while counter <= count:
    line = lines[counter]
    line = line.rstrip('\n')
    linesplit = line.split(' ')
    
    print "Case #" + str(counter) + ": " + get_max_num(linesplit[0], linesplit[1], linesplit[2], linesplit[3:])
    counter += 1

f.close()
