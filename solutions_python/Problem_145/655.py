inpfile = open('C:/Users/Dane/Desktop/CJ/A-small-attempt0 (2).in','r')




def mult():
    Multiples = []
    x = 0
    y = 0
    while (y <1000):
        y = 2**x
        x +=1
        Multiples += [y]
    return Multiples

def comp( num, den):
    dec = num/float(den)
     
    count = 0
    for i in mult():
       
        if (dec * i >= 1):
            return count
        count +=1
def main():
    loop = int(inpfile.readline())

    for i in range (0,loop):
        frac = inpfile.readline()
        fraction = frac.split("/")
        numer = int(fraction[0])
        denom = int(fraction[1])
        if (denom in mult()):
            with  open('C:/Users/Dane/Desktop/CJ/output1c1.txt','a') as out1:
                out1.write( 'Case #%d: %d' % (i+1, comp(numer,denom)))
                out1.write('\n')
        else:
            with  open('C:/Users/Dane/Desktop/CJ/output1c1.txt','a') as out1:
                out1.write( 'Case #%d: impossible' % (i+1))
                out1.write('\n')

main()
          
        
