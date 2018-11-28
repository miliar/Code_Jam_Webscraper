'''
Created on 22 Mei 2010

@author: firman
'''


if __name__ == '__main__':
    
    fin = open("A-large.in","r")
    fout = open("A-large.out","w")
    T = int(fin.readline());
    '''
    Logic here 
    '''
    
    for t in range(1,T+1) :
        count = 0
        N = int(fin.readline())
        
        A=[]
        B=[]
        
        for n in range (N):
            h = fin.readline().split(" ")
            A.append(int(h[0]))
            B.append(int(h[1]))
            
            for z in range (len (A)-1):
                #print ((A[n]-A[z]) /( B[n]-B[z]))
                if (A[n]>A[z] and B[n]>B[z] ) : continue
                elif (A[n]<A[z] and B[n]<B[z] ) : continue
                #elif (A[n]-A[z] / B[n]-B[z] != 1) :
                else : 
                    count = count +1
                    #print count 
                
            
        
        
        #print A,B
        #print "Case #%s: %s\n"%(t,count)
        fout.write( "Case #%s: %s\n"%(t,count))
    
    
    
    
    fout.close()
    fin.close()
    pass