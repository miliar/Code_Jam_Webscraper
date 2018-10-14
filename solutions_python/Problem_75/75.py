name = "B-large"
f_in = open(name + '.in',"r")
f_out = open(name + '.out','w')



T  =  int(f_in.readline())

def makeList(l,Cs,Ds,workstr,N):
        if(N == 0):
                return l
        if(len(l) == 0):
                return makeList([workstr[0]],Cs,Ds,workstr[1:],N-1)

        ch = workstr[0]

        ch1 = l[-1]
        s = ch + ch1
        if s in Cs:
                return makeList(l[:-1],Cs,Ds,Cs[s] + workstr[1:],N)
        
        s = ch1 + ch
        if s in Cs:
                return makeList(l[:-1],Cs,Ds,Cs[s] + workstr[1:],N)

        for x in Ds:
                if ch in x:
                        dch = x[0]
                        if(x[0] == ch):
                                dch = x[1]
                        if(dch in l):
                             return makeList([],Cs,Ds,workstr[1:],N-1)
                        
        return makeList(l+[workstr[0]],Cs,Ds,workstr[1:],N-1)
        
for i in range(T):
        l = [x for x in (f_in.readline().split())]
        C = int(l[0])
        Cs = dict([(x[:2],x[2:])for x in l[1:C+1]])
        D = int(l[C+1])
        Ds = l[C+2:C+2+D]
        N = int(l[C+2+D])
        workstr = l[C+2+D+1]
        
        ret = makeList([],Cs,Ds,workstr,N)
        retS = ""
        for j in range(len(ret)):
                retS += ret[j] + ", "
        if(len(retS)):
                retS = retS[:-2]
                
        f_out.write("Case #" +str(i+1) + ": ["+ str(retS)+"]\n")

 

f_in.close()
f_out.close()
