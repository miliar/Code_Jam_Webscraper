import numpy as np

def solve(M):
    
    return M 
            
# f = file('/home/jabot/Downloads/A-small-attempt2.in');
# fout = file('/home/jabot/Downloads/A-small-attempt2.out','w');

f = file('/home/jabot//workspace2/google_code_jam//A-large.in');
fout = file('/home/jabot/workspace2/google_code_jam/A-large.out','w');

# f = file('/home/jabot/Downloads/A-large.in');
# fout = file('/home/jabot/Downloads/A-large.out','w');

lines = f.readlines();
print lines
T = int(lines[0]);

cnt=0;
li=1;

while cnt<T:

    [D,N] = lines[li].split(' ');
    cnt+=1;
    print '---'
    D = int(D);
    N = int(N);
    li+=1;
    maxt = -1;
    for r in range(N):
        k,s = lines[li].strip().split(' ');
        k = int(k);
        s = int(s);
        li+=1;
        t = float(D-k)/s;
    
        if(t>maxt):
            maxt = t;
            
    fout.write('Case #'+str(cnt)+": "+str(float(D)/maxt)+"\n");
    
fout.close();

