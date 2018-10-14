__author__ = 'rui'
def solve(Smax, auds):
    auds = [int(aud) for aud in auds]
    ret=auds[0]
    res=0
    for i in range(1,len(auds)):
        if ret >=i:
            ret+=auds[i]
        else:
            res+=i-ret
            ret=i+auds[i]
        #print('res: %s , ret: %s'%(res,ret),i)
    return res
infile = 'A-large-practice.in'
infile = 'A-small-attempt0.in'
infile = 'A-large.in'
#infile = 'test.in'
outfile = infile[:infile.find('.')]+'_out1.in'
output = open(outfile,'w')
with open(infile, 'r') as inf:
    n = int(inf.readline().replace('\n',''))
    for i in range(1,n+1):
        line = inf.readline()
        Smax,auds =[x for x in line.replace('\n','').split(' ')]
        #print('new case: ',Smax, auds)
        ret = solve(int(Smax),auds)
        #print(ret)
        tret = 'Case #%s: %s'%(str(i),str(ret))
        output.write(tret+'\n')