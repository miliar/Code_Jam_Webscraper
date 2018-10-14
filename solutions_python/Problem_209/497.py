import numpy as np

def solve(R,H,K):
    
    ### first sort on RH
    RH = R*H;
    sidx = np.argsort(RH)[::-1][:K];
    loi = sidx[-1];

    R2RH = R*R + 2*R*H;
    R2 = R*R;
    hi = np.argmax(R2);
    
    curhi = np.argmax(R[sidx]);
    
    if(hi not in sidx):
        if((R2[hi]-R2[sidx[curhi]])>2*(RH[loi]-RH[hi])):
            sidx[-1]=hi;
    
    maxR = np.max(R[sidx])
    val=np.pi*(np.sum(2*RH[sidx]) + maxR*maxR);
    
    print sidx, R[sidx], H[sidx]
    
    return '%1.10f'%val 

import itertools
def test(R,H,K):
    print R
    print H
    print 'RH', np.pi*2*np.array(R*H,float)
    print 'R2RH', np.pi*np.array(R*R + 2*R*H,float)
    best = -1
    bestopt = [];
    for opts in itertools.combinations(np.arange(len(R)),K):
        
        opts = np.array(opts,int)
        rm = np.max(R[opts])
        new = np.pi*(rm*rm + np.sum(2*R[opts]*H[opts]))
        
        if(new>best):
            best = new;
            bestopt = opts
    
    print bestopt, R[bestopt], H[bestopt]
    
    return best
        
        
f = file('/home/jabot//workspace2/google_code_jam/A-large.in');
fout = file('/home/jabot/workspace2/google_code_jam/A-large.out','w');

lines = f.readlines();
print lines
T = int(lines[0]);

cnt=0;
li=1;

while cnt<T:

    [N,K] = np.array(lines[li].split(' '),int);
    cnt+=1;
    print '---'
    li+=1;
    R=[];
    H=[];
    for ri in range(N):
        r,h = np.array(lines[li].strip().split(' '),int);
        li+=1;
        R.append(r);
        H.append(h);
    
    R = np.array(R);
    H = np.array(H);
    
    outval = float(solve(R,H,K))
#     testval = float(test(R,H,K))
#     print outval
#     print testval
#     assert(np.abs(outval-testval)<1e-08);
    
    fout.write('Case #'+str(cnt)+": "+solve(R,H,K)+"\n");
    
fout.close();

