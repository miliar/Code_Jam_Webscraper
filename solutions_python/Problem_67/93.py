from sys import setrecursionlimit as _srl;
_srl(100000);

def doProb(fname, ofname):
    #do problem A given a file name
    f = open(fname, 'r');
    of = open(ofname, 'w');
    C = int(f.readline());
    output = [];
    for i in range(1,C+1):
        R = int(f.readline());
        d = build([[int(x) for x in f.readline().split()] for i in range(R)]);
        T = 0;
        while(1):
            if (d=={}):
                break;            
            d = update(d);
            T+=1;
            
        tot = T;        
        output.append('Case #' + str(i) + ': ' + str(tot)+'\n');
    f.close();      
    of.writelines(output);
    of.close();


def d_ind(x,y): #gets the diagonal number and offset
    return (x+y, x);

def add_diag(d, n, sf):
    if n in d:
        V = d[n];
        b = False;
        for x in V:
            if(x[0]-1<=sf[1] and sf[0]-1 <= x[1]): #overlap
                b = True;
                x[0] = min(x[0], sf[0]);
                x[1] = max(x[1], sf[1]);
        if(not(b)):
            V.append(sf);                
    else:
        d[n] = [sf];

def build(Coord):
    d = {};
    for R in Coord:
        x_sz = R[2]-R[0]+1;
        y_sz = R[3]-R[1]+1;
        for i in range(x_sz+y_sz-1):
            stx = R[0]+ max(i-y_sz+1, 0);
            sty = R[1]+ min(i, y_sz-1);
            enx = R[0]+ min(i, x_sz-1);
            eny = R[1]+ max(i-x_sz+1, 0);            
            v = [d_ind(stx, sty), d_ind(enx, eny)];
            if(v[0][0] != v[1][0]):
                print('big trouble');            
            add_diag(d, v[0][0], [v[0][1], v[1][1]]);
    return d;

def update(d):
    d2= {};
    for k in d.keys():
        for v in d[k]:
            if(k+1 in d):
                for w in d[k+1]:
                    if(v[0]<=w[1] and w[0] <= v[1]+1):                        
                        add_diag(d2, k+1,[max(v[0], w[0]), min(w[1], v[1]+1)]);                        
            if(v[1]-v[0]>0):
                add_diag(d2, k+1, [v[0]+1, v[1]]);
    return d2;
            

#doProb('C:\Python30\gcj\Round2\C\C_test.in', 'C:\Python30\gcj\Round2\C\C_test.out');
doProb('C:\Python30\gcj\Round2\C\C_small.in', 'C:\Python30\gcj\Round2\C\C_small.out');
#doProb('C:\Python30\gcj\Round2\C\C_large.in', 'C:\Python30\gcj\Round2\C\C_large.out');


