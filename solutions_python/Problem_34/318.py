import sys,re


#ver1 - use prefix trees, generate combinatorially
#       no of candidate msgs, do look up

#ver2- ver1 takes a lot of time.Find out what letters can occur in each posn,
#       and use this info to prune combinatorially generated candidates

#ver3 - some time savings in ver2, but still computationally intensive.
#       Need bactracking... for ex if 'ad*' doesnt exist, then mustnt look for any 'ad*' combination
#       after first such lookup failure.

#Version 3 -final


l,d,n = 0,0,0
posnletters=[]
prefroot={}

#if(len(sys.argv)<2):
#    print 'Need filename'
#    exit()


def readdata(filename,fout):
    global  l,d,n,posnletters
    f=open(filename)
    fw=open(fout,'w')
    caseno=0
    lineno=1
    for line in f:
        line=line.strip()

        if(lineno==1):
            l,d,n = map(lambda(x):int(x),re.compile(r'\s+').split(line))
            for i in range(l):posnletters.append(set([]))
            
        if(lineno >=2 and lineno<=2+d-1):
            createpref(line)
            pos=0
            for letter in line:
                posnletters[pos].add(letter)
                pos+=1
            
        
        if(lineno >=2+d and lineno<=2+d+n-1):
            
            caseno+=1
            print caseno
            c = interpret(line)
            fw.write('Case #%d:%d\n'%(caseno,c))
        lineno+=1
    f.close()
    fw.close()


def createpref(word):
    global prefroot
    curr = prefroot
    for i in word:
        if(i in curr.keys() ):
            curr = curr[i]
            continue
        curr[i]= {}
        curr = curr[i]

def bulkcreate(wordlist):
    for word in wordlist:
        createpref(word)

def mempref(word):
    '''Checks whether given word is present in pref tree.
        Return index at which letter lookup failed.'''
    member = True
    fail_letter_idx=None
    curr=prefroot
    idx=0
    for i in word:
        
        if(i in curr.keys()):
            curr=curr[i]
            
        else:
            member = False
            fail_letter_idx = idx
            break
        idx+=1
    return member,fail_letter_idx
            


def listpref(h,i):
    if(i not in h.keys()): return []
    if(len(h[i])==0): return [i]
    

    arr=[]
    for k in h[i].keys():arr+=listpref(h[i],k)
    return map(lambda(x):'%s%s'%(i,x),arr)



def indexcount(curr,limit,idx):
    '''Tries to modify curr. Returns true for successful modification.
        Else False.
        Increments from idx upwards...everything to its right is set to 0'''
    prev=curr[:]
    if(idx ==None):idx=len(curr)-1
        
    flag=True 
    for i in range(len(curr)-idx,len(curr)+1):
        idx=-1*i
        if(curr[idx]<limit[idx]):
            curr[idx]+=1
            break
        else:
            curr[idx]=0
    if(prev[0]==limit[0] and i==len(curr)):
        for x in range(len(curr)):curr[x]=prev[x]
        #curr=prev
        return False
    else:
        return True

def candidates(msg):
    '''Yields possible words'''
    fullword=[]
    curr=[]
    brack=False
    for i in msg:
        if(i=='('):
            brack=True
            curr=[]
            continue
        if(i==')'):
            brack=False
            fullword.append(curr)
            continue
        if(brack):
            curr.append(i)
        else:fullword.append([i])
    #print fullword
    print map(lambda(x):len(x),fullword)
    #prune fullword using posnletters
    for x in range(len(fullword)):
        tempf=fullword[x]
        pruned=posnletters[x] & set(tempf)
        fullword[x]=list(pruned)
    print map(lambda(x):len(x),fullword)

    
    limit,curr=[],[]
    for arr in fullword:
        limit.append(len(arr)-1)
        curr.append(0)
    if(-1 not in limit):
        loop=True
        while(loop):
            w = createword(curr,fullword)
            flag,fail = mempref(w)
            if(flag):yield w
            loop = indexcount(curr,limit,fail)
        #if(flag)
        #yield createword(curr,fullword)
        #while(indexcount(curr,limit)):
         #   yield createword(curr,fullword)
    

def createword(indices,msg):
    wordarr=[]
    for i in range(len(indices)):
        wordarr.append(msg[i][indices[i]])
    return ''.join(wordarr)

def interpret(msg):
    count=0
    for word in candidates(msg):
        if(mempref(word)):count+=1
    return count
