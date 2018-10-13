def decsum( candies, flags, which ):
    sum = 0
    for i in candies:
        if flags[i] == which:
            sum += candies[i]
    return sum

def xorsum( candies, flags, which ):
    sum = 0
    for i in candies:
        if flags[i] == which:
            sum ^= candies[i]
    return sum

def calcpile( candies, index, sean_dec, patrick_dec, sean_xor, patrick_xor, patrick_empty ):
    if index < len( candies ):
        sd = sean_dec + candies[index]
        sx = sean_xor ^ candies[index]
        thiscandyismine = calcpile( candies, index+1, sd, patrick_dec, sx, patrick_xor, patrick_empty )
        
        pd = patrick_dec + candies[index]
        px = patrick_xor ^ candies[index]

        thiscandyishis = calcpile( candies, index+1, sean_dec, pd, sean_xor, px, False )
        
        return max( thiscandyismine, thiscandyishis )
    else:
        if patrick_empty:
            return -1
        else:
            if sean_xor == patrick_xor:
                return sean_dec
            else:
                return -1
    
def splitpile( candies ):
    return calcpile( candies, 0, 0, 0, 0, 0, True )
    
    
def makeoutput( index, val ):
    s = "Case #"+str(index)+": "
    if val == -1:
        s += 'NO'
    else:
        s += str( val )
    s += '\n'
    return s 

fout = open("output3.txt", "w")
file = []
for line in open( 'sample3.txt', 'r' ):
    file.append( line )
    
ntest = int( file[0] )
j = 1
for i in range( 2, len(file), 2 ):
    r = splitpile( [ int(x) for x in file[i].split(' ') ] )
    fout.write( makeoutput(j, r) )
    j += 1
    
    