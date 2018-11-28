import numpy as np

def getstring(v):

    i=0;
    while(v[i]==0):
        i+=1;    
    return ''.join(np.array(v[i:],'str'));


def solve(l):

    v = np.array([int(x) for x in l]);

    i = len(v)-1;
    s9 = len(v);
    
    carry=0;
    while(i>0):
        v[i] = (v[i]-carry);
        if(v[i]==-1):
            for j in range(i,s9):
                v[j]=9;
            s9 = i;    
            carry=1;
        else:
            carry=0;
        
        if(v[i-1]>v[i]):
            for j in range(i,s9):
                v[j] = 9;
            s9 = i;
            carry=1;
        
        i-=1;
        #print getstring(v);
        
    v[i] = v[i]-carry;
    
    return getstring(v);
    
# f = file('/home/jabot/Downloads/2017_q2_sample.in');
# fout = file('/home/jabot/Downloads/2017_q2_sample.out','w');

# f = file('/home/jabot/Downloads/B-small-attempt0.in');
# fout = file('/home/jabot/Downloads/B-small-attempt0.out','w');

f = file('/home/jabot/Downloads/B-large.in');
fout = file('/home/jabot/Downloads/B-large.out','w');

lines = f.readlines();
print lines
n = int(lines[0]);
cnt=0;
for l in lines[1:n+1]:
    cnt+=1;
    #print np.array(l.strip().split(' ')[1:],int)
    print '---'
    out = solve(l.strip())
    
    print out;
    
    fout.write('Case #'+str(cnt)+": "+out+"\n");
    

