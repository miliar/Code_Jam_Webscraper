
#!/usr/bin/python
# coding=UTF-8

equiv = {
    '1' : 1,
    'i' : 2,
    'j' : 3,
    'k' : 4,
    
    1: '1',
    2: 'i',
    3: 'j',
    4: 'k'
    }
    
mult_rule=[
        [0,0,0,0,0],
        [0,1,2,3,4],
        [0,2,-1,4,-3],
        [0,3,-4,-1,2],
        [0,4,3,-2,-1]
    ]
reduc=0


def solve_dijkstra2(st,m):
    bg=[]
    ed=[]
    inc=[]
    stt=""
    for x in range(m):
        stt+=st
    st=stt
    bgres=1
    bgsign=1
    edres=1
    edsign=1
    for x in range(len(st)):
        #st+=str(equiv[st[x]])
        res=mult_rule[bgres][equiv[st[x]]]
        if res>0:
            bgres=res
        else:
            bgres=-res
            bgsign=-bgsign
        inc.append(bgres*bgsign)
        res=mult_rule[equiv[st[len(st)-x-1]]][edres]
        if res>0:
            edres=res
        else:
            edres=-res
            edsign=-edsign
        if bgres==2 and bgsign == 1:
            bg.append(x)
        if edres==4 and edsign == 1:
            ed.append(len(st)-x-1)
    """print inc
    print bg
    print ed"""
    #print "ok"
    for b in bg:
        for e in ed:
            if b<e:
                """ if e-b>0:
                stt=st[b:e]
                ca=1
                s=1
                for x in range(len(stt)):
                    res=mult_rule[ca][equiv[stt[x]]]
                    if res>0:
                        ca=res
                    else:
                        ca=-res
                        s=-s
                if ca==3:
                    return "YES"
                    """
                if inc[e-1]==4:
                    return "YES"
    return "NO"
            



def solve_dijkstra(st,m):
    reduc=0
    #print "================="
#    print st
    flag_i=False
    flag_j=False
    flag_k=False
    min_length=0
    while min_length<len(st)*4:
        if min_length>0:
            print "restarting with min_length = %d"%(min_length)
            pass
        r=search_quat(st,m,0,2,None,min_length)
        if r==-1:
            return "NO"
        else:
            #print "Found 'i'"
            min_length=r
            r=search_quat(st,m,r,3,4,None)
            if r==-1:
                # Do nothing
                pass
            else:
                #print "Found 'j' & 'k'"
                return "YES"
    return "NO"
    #return (ca,m)
    

def search_quat(st,m,n0,quat,quat2,min_length):
    N=n0%len(st)  # block index
    ct=1    # abs of the result
    s=1     # sign of the result
    found=False
    for n in range(len(st)*2):
        if (n+n0)/len(st)>m+1 :
            return -1
        if n>0 and n%len(st)==0:
            N+=1
        res=mult_rule[ct][equiv[st[(n+n0)%len(st)]]]
        #print "%s%d * %d = %d %s"%("-" if s <0 else "",ct,equiv[st[(n+n0)%len(st)]],res,"[IGNORED]" if n<min_length else "")
        if res>0:
            ct=res
        else:
            ct=-res
            s=-s
        if ct==1 and s==1:
            reduc=n+n0-1
        if ct==quat and s==1 and n>=min_length:
            if quat2 != None :
                #print "Found second and looking for third..."
                # check the rest of the string if quat2 is provided
                if n>=len(st)*m:
                    #print "... but reached past end of string"
                    # we already went past the limit from the test file
                    return -1
                else:
                    ct2=1
                    s2=1
                    n2=((n+n0)+1)
                    while n2<min(1,(m%4))*len(st): #(n2/m)%4!=0 and (n2/m)%4: # n2<len(st)*(((m-1)%4)+1-(n+n0+1)/m):
                        res2=mult_rule[ct2][equiv[st[n2%len(st)]]]
                        #print "%s%d * (%s)%d = %d"%("-" if s2 <0 else "",ct2,st[n2%len(st)],equiv[st[n2%len(st)]],res2)
                        if res2>0:
                            ct2=res2
                        else:
                            ct2=-res2
                            s2=-s2
                        n2+=1
                        #loop til end of string x m
                    if ct2==quat2 and s2==1:
                        #print "Found quats splitting at %d"%(n+n0+1)
                        return n+n0+1
                    else:
                        #print "not found:!"
                        pass

                    # else, keep on looking for quat
            else:
                #pass
                return (n+n0)+1
    return -1

def readfileandsolve_dijkstra(f):
    for t in range(1, int(f.readline())+1):
        # Read testcase
        l=f.readline().strip();
        nst, m = map(int, l.split(" "))
        l=f.readline().strip();
        st = l
        # Solve testcase and output row
        print "Case #%d: %s" % (t, solve_dijkstra2(st,m))
        
#############################################################
f=open("dijkstra_input_0.txt","r")

readfileandsolve_dijkstra(f)
