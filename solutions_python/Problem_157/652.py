index={'1':0,'i':1,'j':2,'k':3,'-1':4,'-i':5,'-j':6,'-k':7}
prod=[['1','i','j','k','-1','-i','-j','-k'],
      ['i','-1','k','-j','-i','1','-k','j'],
      ['j','-k','-1','i','-j','k','1','-i'],
      ['k','j','-i','-1','-k','-j','i','1'],
      ['-1','-i','-j','-k','1','i','j','k'],
      ['-i','1','-k','j','i','-1','k','-j'],
      ['-j','k','1','-i','j','-k','-1','i'],
      ['-k','-j','i','1','k','j','-i','-1']]
test=input()
for _ in range(1,test+1):
    (l,x)=map(int,raw_input().strip().split())
    pat=raw_input().strip()
    pat=pat*x
    p=pat[0]
    i=1
    #print p,
    while p!='i' and i!=l*x:
        p=prod[index[p]][index[pat[i]]]
        #print pat[i],
        i+=1
    if i==l*x:
        print 'Case #{}: {}'.format(_,'NO')
        continue
    
    while True:
        p=pat[i]
        i=i+1
        #print p,
        while i!=l*x and (p!='1' and p!='j'):
            p=prod[index[p]][index[pat[i]]]
        #    print pat[i],
            i+=1
            
        if i==l*x:
            print 'Case #{}: {}'.format(_,'NO')
            break
        elif p=='1':
            continue
        elif p=='j':
            break
    if i==l*x:
        continue
    while i!=l*x:
        p=pat[i]
        i=i+1
        #print p,
        while i!=l*x and (p!='1'):
            p=prod[index[p]][index[pat[i]]]
        #    print pat[i],
            i+=1
    

    if 'k'==p:
        print 'Case #{}: {}'.format(_,'YES')
    else:
        print 'Case #{}: {}'.format(_,'NO')
        
        
