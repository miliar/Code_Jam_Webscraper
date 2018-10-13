import sys
import string

def nl2str(numList):
    return string.join([str(x) for x in numList], '')

####################
fin = open(sys.argv[1])
out = open("nextn_out.txt", "w")

ncases = int( fin.readline() )

for c in range(ncases):
    intro = "Case #%d: " % (c+1)
    #print intro
    out.write(intro)
    
    snum = fin.readline().strip() ## STRIP IS IMPORTANT!!!!!!!!! for \n
    #out.write(snum+"\t\t")
    
    #reset
    lsofar = []
    
    sfinal = ""
    for i in range(len(snum)-1, -1, -1):
        if i == 0:
            #TODO: add stuff for add zero
            #count zeros:
            zeroCount = 0
            if len(lsofar) == 0: # single digit snum
                sfinal = str(snum[0])+'0'
                break
            else:
                for j in range(len(lsofar)):
                    if lsofar[j] == 0:
                        zeroCount +=1
                        if j == len(lsofar)-1: # lsofar=[0] or [0,0]
                            sfinal = str(snum[0])+(zeroCount+1)*'0'
                            break
                    else:
                        lsofar.append(int(snum[0]))
                        lsofar.sort()
                        sfinal = str(lsofar[j])+(zeroCount+1)*'0'+nl2str(lsofar[j+1:])
                        break
                break
        newint = int(snum[i])
        nextint = int(snum[i-1])
        lsofar.append(newint)
        lsofar.sort()
        
        #find if lsofar has a integer that is bigger than nextint
        if nextint < lsofar[-1]: #there must be a bigger than nextint in lsofar
            biggerint = 0
            for k in range(len(lsofar)):
                if nextint < lsofar[k]:
                    biggerint = lsofar[k]
                    lsofar.remove(lsofar[k]) #remove the biggerint from lsofar
                    lsofar.append(nextint)
                    lsofar.sort()
                    sfinal = nl2str(snum[:i-1])+str(biggerint)+nl2str(lsofar)
                    break
            break
    #print sfinal
    out.write(sfinal+"\n")
