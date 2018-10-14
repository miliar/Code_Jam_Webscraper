f = open('input','r')
o = open('output','w')

import time
start = time.time()
N = int(f.readline()[:-1])

d = {'11':('1',False),'1i':('i',False),'1j':('j',False),'1k':('k',False),
'i1':('i',False),'ii':('1',True),'ij':('k',False),'ik':('j',True),
'j1':('j',False),'ji':('k',True),'jj':('1',True),'jk':('i',False),
'k1':('k',False),'ki':('j',False),'kj':('i',True),'kk':('1',True)}

def mul(a,b):
        r=d[a[0]+b[0]]
        s=(a[1] or b[1]) and not(a[1] and b[1])
        s=(r[1] or s) and not(r[1] and s)
        return (r[0],s)
def find_id(v,s,l):
        c=('1',False)
        r=[]
        for i in range(s,len(v)):
                vi=v[i]
                c=mul(c,(vi,False))
                if c == (l,False):
                        r+=[i]
                        if l != 'k':
                                return r
        return r

for Ni in range(N):
        #parse args
        #X = int(f.readline().strip('\n'))
        #I = int(f.readline().strip('\n'))
        l,x = [int(i) for i in f.readline().strip('\n').split(' ')]

        v = f.readline().strip('\n');
        v=v*x
        #print(v)
        #logic
        result = False
        if 'j' not in v and 'k' not in v and len(v) > 2:
                result = False
        else:
                idi=find_id(v,0,'i')
                for i in idi:
                        idj = find_id(v,i+1,'j')
                        for j in idj:
                                idk=find_id(v,j+1,'k')
                                if idk:
                                        if idk[-1]+1 == l*x:
                                                result = True
                                                break
                        if result:
                                break
        #report
        if result:
                result = "YES"
        else:
                result = "NO"
        o.write("case #{0}: {1}\n".format(Ni+1, result))
        print("case #{0}: {1}\n".format(Ni+1, result))
#conclude
o.close()
print("duration {0}".format(time.time()-start))
