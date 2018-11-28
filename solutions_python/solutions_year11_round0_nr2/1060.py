#!/usr/bin/python3

Case=0
inpath='/home/jeff/Downloads/B-large.in'

outpath=inpath.replace('.in','.out')
outfile=open(outpath,'w')
for line in open(inpath):
    line=line.strip()
    if Case==0:
        Case+=1
        continue
    
    case=line.split(' ')
    CombineCount=int(case.pop(0))

    Combine={}
    for c in range(CombineCount):
        t=case.pop(0)
        Combine[t[:2]]=t[2]
    
    Opposed=[]
    OpposedCount=int(case.pop(0))
    for c in range(OpposedCount):
        t=case.pop(0)
        Opposed.append(t)
    
    Invoke=case[-1]
    
    acc=''
    for i in Invoke:
        acc+=i
        for combine in Combine:
            if combine==acc[-2:] or combine[::-1]==acc[-2:]:
                acc=acc[:-2]+Combine[combine]
    
    
        for opposed in Opposed:
            if opposed[0] in acc and opposed[1] in acc:
                acc=''
    print('Case #'+str(Case)+': ' + str([a for a in acc]).replace('\'',''))
    outfile.write('Case #'+str(Case)+': ' + str([a for a in acc]).replace('\'','')+'\n')
    Case+=1
outfile.close()

