import operator
    
def check_parity(n):
    if n==1:
        parity=0
    elif n%2==0:
        parity=1
    else:
        parity=0
    return parity

def group_descpt(group):
    num_i=group[0]
    num_j=-1
    i=1
    j=0
    for aux in group:
        if aux==num_i:
            i+=1
        else:
            if num_j==-1:
                num_j=aux
            j+=1
    return [num_i,i][num_j,j]



fname="C-large.in"
f=open(fname)
T=f.readline()


g = open("output.out", "w")
T=1 


for aux in f:
    N=int(aux.split()[0])
    K=int(aux.split()[1])


    current_g=[[N,1],[N,0]]
    #print current_g
    
    n_g=0
    
    K_bin='{0:b}'.format(K)
    g_n=len(K_bin)-1
    #print K_bin, g_n

    pissing=0
    while n_g<g_n:
        
        
        val=current_g[0][0]
        reps=current_g[0][1]
        
        if check_parity(val)==1:
            reps1=0
            reps2=0
            int_next1=val/2
            reps1=reps1+reps
            int_next2=(val/2)-1
            reps2=reps2+reps
            
            val=current_g[1][0]
            reps=current_g[1][1]
            
            reps2=reps2 + (2*reps)
            
        else:
            reps1=0
            reps2=0
            int_next1=(val-1)/2
            reps1=reps1+(2*reps)
            int_next2=((val-1)/2) - 1
            
            val=current_g[1][0]
            reps=current_g[1][1]
            
            reps1=reps1+reps
            reps2=reps2+reps
            
        #=======================================================================
        # for interval in current_g:
        #     val=interval[0]
        #     reps=interval[1]    
        #     if (check_parity(val)==1):
        #         int_next1=(val/2)
        #         reps1 = reps1+reps
        #         int_next2=(val/2)-1
        #         reps2 = reps2+reps
        #         #print 'if', val
        #     else:
        #         int_next1=val/2
        #         reps1 = reps1+reps*2
        #         int_next2=(val/2)-1
        #         #print 'else', val
        #                 
        # 
        #=======================================================================
        try:
            current_g=[[int_next1,reps1],[int_next2,reps2]]
        except:
            current_g=[[int_next1,reps1]]
            #print 'bergam'
        #print current_g
        pissing = pissing + 2**n_g
        n_g+=1
        
        
        current_g.sort()
        current_g.reverse()
        #print current_g
    
    print 'Case '+str(T)+' - ',(N,K), current_g, K-pissing
    
    if (K-pissing)<=current_g[0][1]:
        if check_parity(current_g[0][0])==1:
            print (current_g[0][0]/2,(current_g[0][0]-1)/2), 'first'
            res=[current_g[0][0]/2,(current_g[0][0]-1)/2]
        else:
            print (current_g[0][0]/2,current_g[0][0]/2), 'second'
            res=[current_g[0][0]/2,current_g[0][0]/2]
            
    else:
        if check_parity(current_g[1][0])==1:
            print (current_g[1][0]/2,(current_g[1][0]-1)/2), 'third'
            res=[current_g[1][0]/2,(current_g[1][0]-1)/2]
        else:
            print (current_g[1][0]/2,current_g[1][0]/2), 'fourth'
            res=[current_g[1][0]/2,current_g[1][0]/2]
    
    print '------'
    

    g.write('Case #'+str(T)+': ' + str(res[0])+ ' ' + str(res[1]) + '\n')
    T+=1

#print K, K_bin
#print N, N_bin, N_bin
#groups[g_n].sort()
#print group_descpt([127,127,128,128,128])
               
        
        