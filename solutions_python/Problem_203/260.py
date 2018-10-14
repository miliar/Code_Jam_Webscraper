import numpy as np


def solve(M):
    
    last_row_done = -1;
    colors = [];
    last_row_colors_saved = [];
        
    for i in range(M.shape[0]):
        last_col_done = -1;
        last_row_colors = [];
        touch = None;
        for j in range(M.shape[1]):
            if(M[i,j]!='?'):
                d = ((last_row_done+1, last_col_done+1),(i,j),M[i,j])
                colors.append(d);
                last_row_colors.append(d)
                last_col_done = j
                touch = M[i,j]
        if(touch!=None):
            d = ((last_row_done+1,last_col_done+1), (i,j), touch)
            colors.append(d);
            last_row_colors.append(d);
            last_row_done = i;
        
        if(len(last_row_colors)>0):
            last_row_colors_saved = last_row_colors;

    print last_row_colors_saved
    lc = 0;
    for ((lrd,lcd), (i,j), c) in last_row_colors_saved:
        colors.append(((i+1,lc),(M.shape[0]-1,j), c));
        lc = j+1
        
    colors.append(((i+1,j+1),(M.shape[0]-1,M.shape[1]-1), last_row_colors_saved[-1][2]));
    
    print colors
    
    for ((sx,sy),(ex,ey),c) in colors:
        for i in range(sx,ex+1):
            for j in range(sy,ey+1):
                M[i,j] = c;
        
    return M 
            

def test(M1, M2):
    
    selInd = (M1!='?');
    
    for i in range(M2.shape[0]):
        for j in range(M2.shape[1]):
            if(selInd[i,j]):
                assert(M1[i,j] == M2[i,j]);
            assert(M2[i,j] != '?');
        
#     for i in range(M2.shape[0]):
#         for j in range(M2.shape[1]):
#             print 

# f = file('/home/jabot/Downloads/A-small-attempt2.in');
# fout = file('/home/jabot/Downloads/A-small-attempt2.out','w');

# f = file('/home/jabot/Downloads/A-sample.in');
# fout = file('/home/jabot/Downloads/A-sample.out','w');

f = file('/home/jabot/Downloads/A-large.in');
fout = file('/home/jabot/Downloads/A-large.out','w');

lines = f.readlines();
print lines
T = int(lines[0]);

cnt=0;
li=1;

while cnt<T:
    [R,C] = lines[li].split(' ');
    cnt+=1;
    print '---'
    R = int(R);
    C = int(C);
    M = np.chararray([R,C])
    li+=1;
    for r in range(R):
        vals = lines[li].strip();
        li+=1;
        for c in range(C):
            M[r,c] = vals[c];

    print M;
    M1 = M.copy();      
    out = solve(M);
    
    print out
    
    test(M1,out);

    fout.write('Case #'+str(cnt)+": "+"\n");
    
    for i in range(M.shape[0]):
        fout.write(''.join(M[i,:])+'\n');
        

fout.close();

