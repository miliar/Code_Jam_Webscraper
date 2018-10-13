import sys

sys.setrecursionlimit(10000)

def ans(S, n):
    if not '-' in S:
        return 0
    else:
        ind=S.index('-') 
        lenS=len(S)
        if ind+n>lenS:
            return 'IMPOSSIBLE'
        else:
            for x in xrange(ind, ind+n):
                if S[x]=='-':
                    S[x]='+'
                else:
                    S[x]='-'
            res=ans(S, n)
            if res!='IMPOSSIBLE':
                return 1+res
            else:
                return 'IMPOSSIBLE'
    


with open ('in.txt') as ifile:
    inp = ifile.readlines()

wfile=open('out.txt', 'w')

t=int(inp[0])
for x in xrange(t):
    res='Case #'+str(x+1)+': '
    L=map(str, inp[x+1].split())
    L[0]=list(L[0])
    L[1]=int(L[1])
    wfile.write(res+str(ans(L[0], L[1]))+'\n')
          
wfile.close()
