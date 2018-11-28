# Const
INPUT_FILE = "input.in"
OUTPUT_FILE = "output.out"

def iSqrt(x):
    if x <= 3 : return [0,1,1,1][x]
    p = x >> 1
    e = ( x//p + p ) >> 1
    
    while e < p:
        p, e = e, ( x//e + e ) >> 1
    
    return p


def iSqrtUp(x):
    if x <= 3 : return [0,1,2,2][x]
    p = x >> 1
    e = ( x//p + p ) >> 1
    
    while e < p:
        p, e = e, ( x//e + e ) >> 1
    
    return (p if (p**2 == x) else p+1)


def isPalin(x):
    x = ' ' + str(x)
    for z in range(len(x)):
        if x[z] != x[-z] : return False
    return True


if __name__ == '__main__':
    fff = open(INPUT_FILE, "r")
    ffg = open(OUTPUT_FILE, "w")
    
    cnt2 = 1
    for inLine in fff:
        cnt = 0
        
        inLine = inLine.split()
        if len(inLine) != 2: continue
        
        x, y = [int(z) for z in inLine]
        x, y = iSqrtUp(x), iSqrt(y)+1
        
        for z in range(x,y):
            if isPalin(z) and isPalin(z**2):
                cnt += 1
        
        ffg.write( "Case #%d: %d\n"%(cnt2, cnt) )
        cnt2 += 1
    
    fff.close()
    ffg.close()
# End of Script