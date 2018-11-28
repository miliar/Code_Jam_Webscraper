import sys



def solv(N , data):
    d = sorted( [ list(j) for j in data.items() ], key = lambda x: -x[1]  )
    
    rlt=[]
    
    if d[0][1] > N/2:
        return "IMPOSSIBLE"
    
    for i in range( d[2][1] ):
        for ii in range(3):
            rlt.append( d[ii][0] )
    
    for tmp in range(3):
        d[tmp][1] -= d[2][1]

    for i in  range( d[1][1] ):
        for ii in range(2):
            rlt.append( d[ii][0] )

    for tmp in range(2):
        d[tmp][1] -= d[1][1]
     
    # last insert
    idx =2  
    for i in range( d[0][1] ):
        rlt.insert(  idx , d[0][0] )
        idx +=4

    return ''.join(rlt)

        

fin = open(sys.argv[1], 'r')
cases = int( fin.readline().strip() )
for i  in range(cases):
    N, R, O, Y, G, B, V  =  map(int,  fin.readline().strip().split() )
    data ={}
    data['R'] = R 
    #data['O'] = O 
    data['Y'] = Y 
    #data['G'] = G 
    data['B'] = B 
    #data['V'] = V 
    print "Case #%d: %s" % ( i+1 , solv(N, data) )
