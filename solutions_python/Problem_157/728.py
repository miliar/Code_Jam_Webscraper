
R=[]

T="smallCaseC.txt"

with open(r'C-small-attempt4.in','rt') as arch:
	for line in arch:
		R.append([str(i) for i in line[0:-1].split()])

t=int(R.pop(0)[0])

Gi={'ii':'-',  'ij':'k' ,  'ik':'-j'}
Gj={'jj':'-',  'ji':'-k',  'jk':'i'}
Gk={'kk':'-',  'ki':'j' ,  'kj':'-i'}

Gim={'-ii':'',  '-ij':'-k',  '-ik':'j'}
Gjm={'-jj':'',  '-ji':'k' ,  '-jk':'-i'}
Gkm={'-kk':'',  '-ki':'-j',  '-kj':'i'}
G={}
G.update(Gi)
G.update(Gk)
G.update(Gj)
G.update(Gim)
G.update(Gkm)
G.update(Gjm)

def lovale(S,m):
    if m=='i':
        if len(S)<4:
            if len(S)==2:
                return False
            elif S[0]!='i':
                return False
    if m=='j':
        if len(S)<3:
            if len(S)==0:
                return False
            elif S[0]!='j':
                return False
    if m=='k':
        if len(S)==1:
            if S!='k':
                return False
    if m=='':
        if len(S)==1:
            return False
        elif len(S)==2 and S[0]=='-':
            return False
    else: 
        return True

def obtiene(S,n):
    if n=='':
        while len(S)>1:
            if S[0]=='-' and len(S)>2:
#                print '<<<',S
                S=S=G[S[0:3]]+S[3:]
#                print '>>>',S
            elif S[0]=='-' and len(S)<3:
                return False
            else:
#                print '<<<',S
                S=G[S[0:2]]+S[2:]
#                print '>>>',S
        if S!='':
            return False
        else:
            return S
    if S[0]==n:
        return S[1:]
    else:
        if lovale(S,n)==False:
            return False
        else:
            while S[0]!=n:
                if S[0]=='-' and len(S)>2:
    #                print '<<<',S
                    S=G[S[0:3]]+S[3:]
    #                print '>>>',S
                    if lovale(S,n)==False:
                        return False
                elif S[0]=='-' and len(S)<3:
                    return False
                else:
    #                print '<<<',S
                    S=G[S[0:2]]+S[2:]
                    if lovale(S,n)==False:
                        return False
    #                    print '>>>',S
            return S[1:]


def taco(S):
#    print S,'i'
    S=obtiene(S,'i')
    if S==False:
        return 'NO'
    else:
#        print S,'j'
        S=obtiene(S,'j')
        if S==False:
            return 'NO'
        else:
#            print S,'k'
            S=obtiene(S,'k')
            if S==False:
                return 'NO'
            else:
#                print S,'------'
                if len(S)==0:
                    return 'YES'
                else:
                    S=obtiene(S,'')
                    if S==False:
                        return 'NO'
                    else:
                        return 'YES'

filee=open(T,'w')

for i in range(t):
#    print '**************************************************'
    Z1=map(int,R.pop(0))
    Z=Z1[1]
    w=R.pop(0)[0]
    word=w*Z
    if len(word)<3 and word!='ijk':
        filee.write('Case #%i: %s' %(i+1,'NO'))
        filee.write('\n')
        
    else:
        F=taco(word)
        filee.write('Case #%i: %s' %(i+1,F))
        filee.write('\n')
        print i+1,F
filee.close()
        
        
        
        
        
        
        
        
        
        
