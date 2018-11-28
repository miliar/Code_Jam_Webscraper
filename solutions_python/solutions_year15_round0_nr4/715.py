__author__ = 'rui'
def solve(X,R,C):
    if X==1:
        return 'GABRIEL'
    if R*C%X==1:
        return 'RICHARD'
    else:
        #print('X,R,C',X,R,C,R%X,C%X)
        #print (R!=0 and R%X==0 and C>=2)or (C!=0 and C%X==0 and R >=2)
        return 'GABRIEL' if (R!=0 and R%X==0 and C>=X-1)or (C!=0 and C%X==0 and R >=X-1) else 'RICHARD'

infile = 'D-large-practice.in'
infile = 'D-small-attempt1.in'
#infile = 'testD.in'
outfile = infile[:infile.find('.')]+'_out1.in'
#print(outfile)
output = open(outfile,'w')
with open(infile, 'r') as inf:
    n = int(inf.readline().replace('\n',''))
    for i in range(1,n+1):
        X,R,C = [int(x) for x in inf.readline().replace('\n','').split(' ')]
        #print ('new case',X,R,C)
        ret = solve(X,R,C)
        #print(ret)
        tret = 'Case #%s: %s'%(str(i),str(ret))
        output.write(tret+'\n')