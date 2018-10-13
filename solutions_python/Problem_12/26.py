
def Solve(seq):
        c = 1000000007
        n = len(seq)
        dct={}
        for i in range(n-1,-1,-1):
                collect = 1
                for j in dct.keys():
                        if j>seq[i]:
                                collect += dct[j]
                                collect = collect % c
                if not(dct.has_key(seq[i])):
                        dct[seq[i]]=collect
                else:
                        dct[seq[i]]+=collect
        tot = 0
        for k in dct.keys():
                tot+=dct[k]
                tot=tot%c
        return tot        
                            
                        
#--------------------

def main():
        f=open('c:\\Python25\\Scripts\\inputfile.txt','r')      
        fout=open('c:\\Python25\\Scripts\\outputfile.txt','w')
        N=int(f.readline())
        print N
        for i in xrange(1,N+1):
                l = f.readline()
                l = l.split()
                n = long(l[0])
                m = long(l[1])
                X = long(l[2])
                Y = long(l[3])
                Z = long(l[4])
                a=[]
                for j in range(1,m+1):
                        l = f.readline()
                        a.append(long(l))
                seq = []
                for j in range(0,n):
                        seq.append(a[j%m])
                        a[j%m]= (X * a[j%m] + Y * (j + 1))%Z
                #print seq        
                result = int(Solve(seq))
                fout.write('Case #'+repr(i)+': '+repr(result)+'\n')    
        f.close()
        fout.close()
