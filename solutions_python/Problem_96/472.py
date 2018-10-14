import io
import math

def CalculateMax(data):
    s = data.split(' ')
    out = 0
    count = int(s[0])
    surprise = int(s[1])
    best = int(s[2])
    totallist = []
    
    for i in range(3, count + 3):
        totallist.append(int(s[i]))
    
    for total in totallist:
        quo = total/3
        rem = total%3
        if (total==0 and best > 0) or (best + (best - 2)*2 > total):
            # do nothing
            total = 0
        elif (quo >= best) or (rem > 0 and quo + 1 >= best):
            out = out + 1        
        elif (rem == 0 and quo + 1 >= best and surprise > 0) or (rem == 2 and quo + 2 >= best and surprise > 0):
            out = out + 1
            surprise = surprise - 1
    return str(out)        

fin = open('in', 'r')
fout = open('out', 'w')
j = 0
for line in fin:
    if (j > 0):
        out = CalculateMax(line)         
        fout.write('Case #' + str(j) + ': ' + out + '\n')        
    j = j + 1
fin.close()    
fout.close()


