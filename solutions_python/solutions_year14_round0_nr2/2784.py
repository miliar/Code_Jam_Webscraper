def Best( C , F , X ):
    T , R = 0 , 2.0
    while True:
        Rnew = R + F
        Should = ((X-C)/R) > (X/Rnew)
        if Should:
            T += (C/R)
            R = Rnew                
        else:
            T += (X/R)
            return T
Output = ''
with open('B-large.in','r') as ReadO:
    Total = ReadO.read().split('\n')
    Stop = int(Total[0])
    for i,Line in enumerate(Total[1::]):
        C , F , X = Line.split(' ')
        C , F , X = float(C),float(F),float(X)
        Output += 'Case #%s: %s\n' % (i+1,Best(C,F,X))
        if i+1==Stop:
            break
with open('Outfile.txt','w') as Out:
    Out.write(Output)
        
        
    
    
