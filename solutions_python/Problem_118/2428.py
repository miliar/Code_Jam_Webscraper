import math
def sayiIncele(f,case,f2):
    x=[]
    line=f.readline().split()
    line= [ long(x) for x in line ]
    #print line

    countP=0
    i=line[0]
    j=int(math.sqrt(line[0]))+1


    while 1==1:
        if i > line[1]: break
        if str(i)[::-1]==str(i) and math.sqrt(i)%1==0:
            #print >>f2, i
            countP+=1
        i=j**2
        j+=1

    
##    for i in xrange(line[0],line[1]+1):
##       if str(i)[::-1]==str(i):
##           if math.sqrt(i)%1==0:
##               print i
##               countP+=1
    print >>f2, "Case #"+str(case)+": "+str(countP)
    
    


def main():
    f = open('C-small-attempt0.in')
    f2 = open('C-small-attempt0.out','w+')
    #case oku
    lines = f.readline()
    case = int(lines)

    for i in range(case):
        sayiIncele(f,i+1,f2)


main()
