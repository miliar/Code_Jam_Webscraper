'''
Created on May 23, 2010

@author: mogox
'''


dbg=True
outfilename= 'a-large.out'
outfile = open(outfilename, 'w+')

def log(str):
    if(dbg):
        print str
    
def write(str):
    print str
    outfile.write(str+"\n")

t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    a=[]
    b=[]
    x=[]
    total=0
    for j in range(n):
        values=(raw_input()).split(' ')
        a.append(int(values[0]))
        b.append(int(values[1]))
        if(a[j]!=b[j]):
            x.append(j)
    dic={}
    for k in x:
        l=a[k]
        r=b[k]
        for j in range(n):
            s=set([])
            if j==k:
                continue
            elif dic.has_key(j):
                s1=dic[j]
                if k in s1:
                    continue
            else:
                if l>=a[j] and r<=b[j]:
                    total+=1
                    mem=True
                elif l<=a[j] and r>=b[j]:
                    total+=1
                    mem=True
                s.add(j)
                if mem:
                    if dic.has_key(k):
                        dic[k].union(s)
                    else:
                        dic[k]=set([])
                        dic[k].update(s)
                
    write('Case #'+str(i+1)+': '+str(total))
    
    
    