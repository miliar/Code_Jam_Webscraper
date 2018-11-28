__author__ = 'rui'
def solve(dn, panlst):
    if len(panlst)==1 and panlst[0]<4:
        return panlst[0]
    ret = 0
    pandct={}
    for i in panlst:
        if i not in pandct:
            pandct[i]=0
        pandct[i]+=1
    #print('frequency',pandct)
    panlst = sorted(pandct)
    print('sorted',panlst)
    MX = panlst[-1]
    mx = panlst[-1]
    smx = panlst[-2] if len(panlst)>1 else 0

    while not isContinuous(panlst) or pandct[mx]<=min(mx//2,mx-mx//2):
        h1 = mx//2
        h2 = mx-h1
        print(h1,h2,pandct[mx])
        if pandct[mx]<min(h1,h2):
            print('updated')
            panlst.pop()
            panlst.append(h1)
            panlst.append(h2)
            panlst = sorted(list(set(panlst)))
            ret+=1*pandct[mx]
            mx = panlst[-1]
            smx = panlst[-2]if len(panlst)>1 else 0
            if h1 not in pandct:
                pandct[h1]=0
            pandct[h1]+=1
            if h2 not in pandct:
                pandct[h2]=0
            pandct[h2]+=1
        else:
            break

        print ('ret',ret)
    print ('ret',ret+mx if ret else mx)
    return min(ret+mx,MX) if ret else mx
def isContinuous(plst):
    pre = plst[-1]
    for p in plst[::-1][1:]:
        if pre-p<=1:
            pre = p
        else:
            return False
    return True
hs = {}
def solve_brute(dn,panlst):
    if tuple(panlst) in hs:
        return hs[tuple(panlst)]
    #print('new call',dn,panlst)
    if len(panlst)==0:
        return 0
    ret = max(panlst)
    eat = [x-1 for x in panlst if x-1>0]
    eatret=1+solve_brute(len(eat),eat)
    ret = min(eatret,ret)
    mx = max(panlst)
    for d in range(dn):
        p=panlst[d]
        #print('current',p,panlst)
        if p <=1 and p<mx:
            continue
        for i in range(1,p):
            #print('new list',panlst[:d]+panlst[d+1:]+[i,p-i])
            newpanlst = sorted(panlst[:d]+panlst[d+1:]+[i,p-i])
            tmp = 1+solve_brute(dn+1,newpanlst)
            ret = min(ret,tmp)
            #print ('ret',ret,i,p-i)
    hs[tuple(sorted(panlst))]=ret
    return ret
infile = 'B-large-practice.in'
infile = 'B-small-attempt3.in'
#infile = 'testB.in'
outfile = infile[:infile.find('.')]+'_out_brute.in'
output = open(outfile,'w')
#output1 = open('B-small-attemp0_clean.txt','w')
with open(infile, 'r') as inf:
    n = int(inf.readline().replace('\n',''))
    for i in range(1,n+1):
        for j in range(2):
            tmp = inf.readline().replace('\n','')
            #output1.write('new case:'+'\t')
            if j ==0:
                dn = int(tmp)
                #output1.write('\t'.join(tmp.split(' '))+'\t')
            else:
                panlst = [int(x) for x in tmp.split(' ')]
                #output1.write('\t'.join(tmp.split(' '))+'\n')
        #print('new case',i, dn , panlst)
        panlst = sorted(panlst)
        ret = solve_brute(dn, panlst)
        #print(ret)
        tret = 'Case #%s: %s'%(str(i),str(ret))
        output.write(tret+'\n')