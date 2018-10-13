'''
Created on 14 Apr 2012

@author: rich
'''

def recyclednumbers(fin,fout):
    f = open(fin,'r')
    fout = open(fout,'w')
    
    is_first = True
    t = 1
    for r in f:
        if is_first:
            T = r
            is_first = False
        else:
            arr = r.split(' ')
            A = int(arr[0])
            B = int(arr[1])
            print A,B
            n = get_recycled_pairs(A,B)
            fout.write('Case #' + str(t) + ': ' + str(n) + '\n')
            t += 1
        
        print t
    
def get_recycled_pairs(A,B):
    ints = {}
    for i in range(A,B+1):
        s = get_sorted_int(i)
        if ints.has_key(s):
            ints[s].append(i)
        else:
            ints[s] = [i]
    
    print ints
    cyclic_pairs = []
    for s in ints.keys():
        a = ints[s]
        l = len(s)
        al = len(a)
        if al>1:
            for j in range(0,al-1):
                for k in range(j+1,al):
                    if is_cyclic_pair(a[j],a[k],l):
                        cyclic_pairs.append([a[j],a[k]])
        
    #print cyclic_pairs
    #print len(cyclic_pairs)
    return len(cyclic_pairs)
            
    
def get_sorted_int(i):
    s = str(i)
    a = []
    for j in range(0,len(s)):
        a.append(s[j:j+1])
    a.sort()
    return ''.join(a)

def is_cyclic_pair(i,j,l):
    
    a = str(i)
    b = str(j)    

    # find all the matches in b for the first char of a
    matches = {}
    for i in range(l):
        m = b.find(a[0],i)
        if m > -1 and not matches.has_key(m):
            matches[m] = ''
    
    for offset in matches.keys():
        is_cyclic = True
        for k in range(1,len(a)):
            if b[(offset + k)%l] <> a[k]:
                is_cyclic = False
                break
        if is_cyclic == True:
            break
        
    return is_cyclic

def dancingwithgooglers(fin,fout):
    f = open(fin,'r')
    fout = open(fout,'w')
    
    is_first = True
    t = 1
    for r in f:
        if is_first:
            T = int(r)
            is_first = False
        else:
            arr = r.split(' ')
            N = int(arr[0])
            S = int(arr[1])
            p = int(arr[2])
            
            ti = []
            for x in arr[3:]:
                ti.append(int(x))
                
            #print N,S,p,ti
            
            n = getdancingn(N,S,p,ti)
            
            fout.write('Case #' + str(t) + ': ' + str(n) + '\n')
            t += 1
        
        print t    

def getdancingn(N,S,p,ti):
    
    # assume that the suprises were on the highest total
    
    # unsurprising triplets
    # ---------------------
    # if t is divisible by 3 then the highest score from an unsurprising result is
    # t/3 ( as the triplet will be t/3, t/3, t/3)
    # e.g. t=6, 2,2,2
    # any other triplet would be surprising 
    
    # if t%3 = 1, e.g. 7 then the highest score from the triplet is t-t%3/3+1
    # or 1+(t-1)/3
    # (t-1)/3 t-1/3 (t-1/3)+1
    # e.g. 2,2,3
    
    # if t%3 = 2 e.g 8, then the highest score from the triplet is t+1/3:
    # (t+1)/3, (t+1)/3 (t+1)/3-1
    # e.g. 3,3,2
    
    # surprising triplets
    # -------------------
    # t%3 = 0
    # max is 1+t/3
    
    # t%3 = 1, e.g. 7
    # max is 1,3,3 = 3 = 1+(t-1)/3 
    
    # t%3 = 2, e.g. 8
    # max is 4,2,2, so 1+(t+1)/3
    
    # in summary:
    # t%3|unsurprising max| surprising max
    #----|----------------|---------------
    # 0  |    t/3         |   1+t/3
    # 1  |    1+(t-1)/3   |   1+(t-1)/3
    # 2  |    (t+1)/3     |   1+(t+1)/3
    
    
    # so strategy is:
    # 1. calculate the unsuprising max for each ti and create an arrays maxs
    # 2. calculate the surprising max for each ti
    # 3. assign the surprising maxs to the S highest totals in maxs
    # 5. count how many element in maxs are >= p
    
    maxs = []
    for t in ti:
        if t==0:
            maxs.append(0)
        else:
            if t%3 == 0:
                maxs.append(t/3)
            elif t%3 == 1:
                maxs.append(1+(t-1)/3)
            elif t%3 == 2:
                maxs.append((t+1)/3)
        
    #print ti,maxs
    
    surps={}
    ptr=0
    smax=0
    for t in ti:
        if t==0:
            smax=0
        else:         
            if t%3 == 0:            
                smax = 1+t/3
            elif t%3 == 1:
                smax = 1+(t-1)/3
            elif t%3 == 2:
                smax = 1+(t+1)/3        
        
        if surps.has_key(smax):
            surps[smax].append(ptr)
        else:
            surps[smax] = [ptr]
        
        ptr+=1
        
    #print surps
    
    # sort the max keys
    smaxs = surps.keys()
    smaxs.sort()
    smaxs.reverse()
    
    j=0
    smaxidx=0
    ptridx=0
        
    while j<S and smaxidx<len(smaxs):
        #print smaxidx,ptridx
        ptr=surps[smaxs[smaxidx]][ptridx]
        if maxs[ptr]<p and smaxs[smaxidx]>=p:
            maxs[ptr]=smaxs[smaxidx]
            j+=1
        
        if ptridx==len(surps[smaxs[smaxidx]])-1:
            ptridx=0
            smaxidx+=1
        else:
            ptridx+=1
           
    # now count the number of elements in maxs >= p
    c=0 
    #print ti,maxs,smaxs,surps
    for m in maxs:
        if m>=p:
            c+=1
    
    return c
        
    
    
    





if __name__ == '__main__':
    pass

fin = 'C:\\Users\\rich\\Documents\\codejam\\B-large.in'
fout = 'C:\\Users\\rich\\Documents\\codejam\\B-large.out'
dancingwithgooglers(fin,fout)

#print is_cyclic_pair(203,302,3)
#s = get_sorted_int(12345)
#print s,len(s)
