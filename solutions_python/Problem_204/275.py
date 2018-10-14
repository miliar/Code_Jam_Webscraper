import numpy as np


def solve(Q, rec):

    H = np.zeros_like(Q);
    L = np.zeros_like(Q);
    
    for i in range(len(rec)):
        H[i,:] = np.floor(Q[i,:]/(0.9*rec[i]));
        L[i,:] = np.ceil(Q[i,:]/(1.1*rec[i]));
        
        sidx = np.argsort(H[i,:]);
        H[i,:] = H[i,sidx];
        L[i,:] = L[i,sidx];
    
    N = Q.shape[0];
    idx = np.zeros(N,int);
    
    l = L[:,0];
    h = H[:,0];
    
    print 'H=', H
    print 'L=', L
    
    ### from l to h
    
    P = Q.shape[1];
    cnt = 0;
    
    list_out = [];
    while(True):
        
        min_hi = np.argmin(h);
        max_li = np.argmax(l);
        
        min_h = h[min_hi];
        max_l = l[max_li];
        
        if(min_h>=max_l):
            cnt+=1;
            list_out.append(idx.copy());
            
            idx+=1;
            if(np.max(idx)==P):
                break;
            h = np.array([H[i,idx[i]] for i in range(N)]);
            l = np.array([L[i,idx[i]] for i in range(N)]);
            
        else:
            idx[min_hi]+=1;
            if(idx[min_hi]==P):
                break;
#             print min_hi, idx[min_hi]
            l[min_hi]=L[min_hi,idx[min_hi]];
            h[min_hi]=H[min_hi,idx[min_hi]];
    
    print cnt
    
    if(cnt>0):
        list_out = np.array(list_out);
        
        for idx in list_out:
            print idx
            h = [H[i,idx[i]] for i in range(N)]
            l = [L[i,idx[i]] for i in range(N)]
            
            assert(np.min(h)>=np.max(l));
            
        for j in range(N):
            assert(len(np.unique(list_out[:,j]))==list_out.shape[0]);
        
    return cnt;
        
# f = file('/home/jabot/Downloads/B-sample.in');
# fout = file('/home/jabot/Downloads/B-sample.out','w');

f = file('/home/jabot/Downloads/B-small-attempt1.in');
fout = file('/home/jabot/Downloads/B-small-attempt1.out','w');

# f = file('/home/jabot/Downloads/B-large.in');
# fout = file('/home/jabot/Downloads/B-large.out','w');

lines = f.readlines();
print lines
T = int(lines[0]);

cnt_t=0;
li=1;

while cnt_t<T:
    
    cnt_t+=1;
    N,P = lines[li].strip().split(' ');

    N = int(N);
    P = int(P);
    
    li+=1;
    rec = np.array(lines[li].strip().split(' '),float);
    
    li+=1;
    Q = np.zeros([N,P]);
    for n in range(N):
        Q[n,:] = np.array(lines[li].strip().split(' '),float);
        li+=1;
    
    print '-----'
#     print rec
#     print Q
    out = solve(Q, rec);
    
    fout.write('Case #'+str(cnt_t)+": "+str(out)+"\n");

fout.close();

