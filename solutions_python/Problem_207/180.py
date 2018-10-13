import numpy as np

def solveSimple(B,R,Y):

    counts = np.array([B,R,Y]);
    idx = np.argsort(counts);
    counts = counts[idx];
    names = np.array(['B', 'R', 'Y'])[idx];

    if(counts[2]>counts[0]+counts[1]):
        return [];
    else:
        totalYRB=(counts[0]+counts[1])-counts[2];
        totalRB=(counts[0]-totalYRB);
        totalRY=(counts[1]-totalYRB);
    
        print totalYRB
        print totalRB
        print totalRY
        if(totalRB>0):
            return np.hstack([
                              np.tile([names[2],names[1]], totalRY),
                              np.tile([names[2],names[0]], totalRB),
                              np.tile([names[1],names[2],names[0]], totalYRB)
                              ]);
        else:
            return np.hstack([
                              np.tile([names[2],names[0]], totalRB),
                              np.tile([names[2],names[1]], totalRY),
                              np.tile([names[0],names[2],names[1]], totalYRB)
                                ]);


def test(ls, R, B, Y):
    
    if(len(ls)==0):
        return
    
    print ls, R, B, Y
    ls = np.array(ls);
    assert (np.sum(ls=='R')==R)
    assert (np.sum(ls=='B')==B)
    assert (np.sum(ls=='Y')==Y)
    
    assert(np.sum(ls[1:]==ls[:-1])==0)
    
    
s = {};
def solve(N,R,O,Y,G,B,V):

    print N, R, O, Y, G, B, V

    #### finish the O,G,V
    B1=0;
    R1=0;
    Y1=0;

    if(B+O>0):
        if(B>O):
            B1 = B-O;
            s['B'] = ''.join(np.repeat('BO',O))+'B';
        elif(B<O):
            return 'IMPOSSIBLE'
        else:
            if(N!=B+O):
                return 'IMPOSSIBLE';
            else:
                return ''.join(np.repeat('BO',N/2));

###-----
    if(R+G>0):
        if(R>G):
            R1 = R-G;
            s['R'] = ''.join(np.repeat('RG',G))+'R';
        elif(R<G):
            return 'IMPOSSIBLE'
        else:
            if(N!=R+G):
                return 'IMPOSSIBLE';
            else:
                return ''.join(np.repeat('RG',N/2));

####---
    if(Y+V>0):
        if(Y>V):
            Y1 = Y-V;
            s['Y'] = ''.join(np.repeat('YV',V))+'Y';
        elif(Y<V):
            return 'IMPOSSIBLE'
        else:
            if(N!=Y+V):
                return 'IMPOSSIBLE';
            else:
                return ''.join(np.repeat('YV',N/2));

    ls = solveSimple(B1,R1,Y1);
    
    test(ls, R1,B1,Y1)
    
    if(len(ls)==0):
        return 'IMPOSSIBLE';
    
    print ls
    print s
    
    ls2 = [];
    for v in ls:
        if(v=='R'):
            if ('R' in s):
                ls2.append(s['R']);
                del s['R'];
            else:
                ls2.append('R');
        if(v=='B'):
            if ('B' in s):
                ls2.append(s['B']);
                del s['B'];
            else:
                ls2.append('B');
        if(v=='Y'):
            if ('Y' in s):
                ls2.append(s['Y']);
                del s['Y'];
            else:
                ls2.append('Y');
                
    
    return "".join(ls2);
            
# f = file('/home/jabot/Downloads/B-small-attempt2.in');
# fout = file('/home/jabot/Downloads/B-small-attempt2.out','w');

# f = file('/home/jabot/Downloads/B-sample.in');
# fout = file('/home/jabot/Downloads/B-sample.out','w');

f = file('/home/jabot//workspace2/google_code_jam//B-large.in');
fout = file('/home/jabot/workspace2/google_code_jam/B-large.out','w');

lines = f.readlines();
print lines
T = int(lines[0]);

cnt=0;
li=1;

while cnt<T:

    print '----'

    [N, R, O, Y, G, B, V] = np.array(lines[li].split(' '),int);
    cnt+=1;
    li+=1;

    out = solve(N,R,O,Y,G,B,V);
    
    print out
    
    fout.write('Case #'+str(cnt)+": "+out+"\n");
    

fout.close();

