from string import *

def compute( A, B, p ):
    strikes = B+2
    #print strikes
    for i in range (int(A)+1):
        perc = 1
        for num in range (len(p)-i):
           # print "num:",p[num],
            perc *= float(p[num])
        
        temp = perc*(B-A+2*i+1) + (1-perc)*(2*B-A+2*i+2)
       # print perc,"*",(B-A+2*i+1),"+",(1-perc),"*",(2*B-A+2*i+2),"=",temp
        #print i, temp
        if temp < strikes:
            strikes = temp
    return strikes

fileName = raw_input("File name: ")
f = open(fileName,"r")

n = int(f.readline()[:-1])



for i in range(n):
    items = (f.readline()[:-1]).split()
    p = (f.readline()[:-1]).split()
    #print "A,B",items, "Perc",p
    print "Case #%d: %.6f" %(i+1, compute( float(items[0]), float(items[1]), p ) )
         
    # read in each line

f.close()


    
    


    
