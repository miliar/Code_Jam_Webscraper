import sys

def calc(lstCombine,lstOpposed,lstInput):
    if len(lstInput)==1 or (not lstCombine and not lstOpposed):
        return ', '.join(lstInput)
    dicCombine=dict([(s[:2],s[-1]) for s in lstCombine])
    dicCombine.update(dict([(s[1]+s[0],s[-1]) for s in lstCombine]))
    dicOpposed=dict([(s,0) for s in lstOpposed])
    dicOpposed.update(dict([(s[1]+s[0],0) for s in lstOpposed]))
    dicSuspicious={}
    for s in lstOpposed:
        dicSuspicious[s[0]]=0
        dicSuspicious[s[1]]=0
    buf=[]
    dicWatchList={}
    for c in lstInput:
        if not buf:
            buf.append(c)
            if c in dicSuspicious:
                dicWatchList[c]=dicWatchList.get(c,0)+1
            continue
        if buf[-1]+c in dicCombine:
            tmp=buf.pop()
            if tmp in dicWatchList:
                dicWatchList[tmp]-=1
                if dicWatchList[tmp]==0:
                    del dicWatchList[tmp]
            buf.append(dicCombine[tmp+c])
            continue
        if buf[-1]+c in dicOpposed:
            buf=[]
            dicWatchList={}
            continue
        if c in dicSuspicious:
            for key in dicWatchList:
                if key!=c and key+c in dicOpposed:
                    buf=[]
                    dicWatchList={}
                    break
            if not buf:
                continue
        buf.append(c)
        if c in dicSuspicious:
            dicWatchList[c]=dicWatchList.get(c,0)+1
    return ', '.join(buf)

def main():
    f=file(sys.argv[1])
    T=int(f.readline().strip())
    fOut=file('output.txt','wb')
    for i in range(1,1+T):
        s=f.readline().strip()
        if not s: continue
        lst=s.split(' ')
        lstCombine=[]
        lstOpposed=[]
        lstInput=[c for c in lst[-1]]
        num = int(lst.pop(0))
        if num:
            lstCombine=lst[:num]
            lst=lst[num:]
        num = int(lst.pop(0))
        if num:
            lstOpposed=lst[:num]
        output=calc(lstCombine,lstOpposed,[c for c in s.split(' ')[-1]])
        line='Case #%s: [%s]\r\n'%(i,output)
        print line
        fOut.write(line)
    fOut.close()
    
if __name__=='__main__':
    main()