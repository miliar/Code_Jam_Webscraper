vector=[]
for i in range(10000):
    
    if i<10:
        vector.insert(len(vector),i)
    else:    
        string = str(i)
        ordenado = sorted(string)
        stringOrdenado = "".join(str(elm) for elm in ordenado)       
        if(string == stringOrdenado):
            vector.insert(len(vector),i)
        if(i<int(stringOrdenado)):
            vector.insert(len(vector),i)
        
t = int(raw_input()) 
for i in xrange(1, t + 1):
    for j in raw_input().split("\n"):
        cont=-1
        for k in vector:            
            if(int(j)<k):
                print "Case #{}: {}".format(i,vector[cont])
                break
            cont+=1
        
        
            
        
