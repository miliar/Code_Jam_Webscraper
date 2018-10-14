'''
Created on 12-Apr-2014

@author: tadikond
'''    
from collections import deque

def optimalgame(N,naomi,ken):
    naomi=deque(naomi)
    ken=deque(ken)
    naomipoints=0
    kenpoints=0
    while N>0:
        chosennaomi=naomi.pop()
        if max(ken)<chosennaomi:
            chosenken=ken.popleft()
            naomipoints+=1
        else:
            chosenken=ken.pop()
            kenpoints+=1
        N-=1
    return naomipoints

def deceitfulgame(N,naomi,ken):
    naomi=deque(naomi)
    ken=deque(ken)
    naomipoints=0
    kenpoints=0
    while N>0:
        if max(naomi)>max(ken):
            toldnaomi=max(naomi)
            choseken=ken.popleft()
            chosennaomi=naomi.remove(min([a for a in naomi if a>choseken]))
            naomipoints+=1
        else:
            toldnaomi=max(ken)-0.00001
            chosennaomi=naomi.popleft()
            choseken=ken.pop()
            kenpoints+=1
        N-=1
    return naomipoints

def Deceitfulwar(t,fin,fout):
    N=int(fin.readline())
    naomi=[float(a) for a in fin.readline().split(" ")]
    ken=[float(a) for a in fin.readline().split(" ")]
    naomi.sort(cmp=None, key=None, reverse=False)
    ken.sort(cmp=None, key=None, reverse=False)
    result=str(deceitfulgame(N,naomi,ken))+' '+str(optimalgame(N,naomi,ken))+'\n'
    fout.write("Case #"+str(t)+": "+str(result))
    
     
def main(fin,fout):
    T=int(fin.readline())
    for t in range(T):
        Deceitfulwar(t+1,fin,fout)
        
if __name__ == '__main__':
    fin=open("D-large.in","r")
    fout=open("D-large.out","w")
    main(fin,fout)
    fin.close()
    fout.close()