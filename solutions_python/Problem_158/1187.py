"""
'Ominous Omino', Google Codejam qualification round problem D.

Given X,R,C, determine if an R x C grid can be tiled with X-ominoes
if we're required to use one maximally inconvenient X-omino.

This is simple unless X is such that we can fit the worst X-omino,
but there is an X-omino that can be picked which, when placed,
partitions the grid into two separate regions.
In this case, it is not immediately clear whether the separate regions
can be tiled with X-ominos or not.
Now, such regions can be tiled iff they're of size  

"""


def canTile(X,R,C):
    #print(X,R,C)
    R,C = min(R,C), max(R,C); #for convenience
    if R*C % X: return False; #can't tile with X-ominos
    if X > C: return False; #broken by long X-omino
    if R > (X+1)//2: return True #can't partition
    if R < (X+1)//2: return False #can't fit
    #print("Can partition.")
    #else R = (X+1)//2 = ceiling(X/2).
    #In which case any X-omino will fit, but there exist
    #a class of X-ominos which partition the grid.
    if X % 2: #need enough shifts to cover residues (mod X)
        num_residues = min(X, R*(X-R+1) - X + 1);
        num_shifts = C - R;
        #print("%d residues, %d shifts" % (num_residues,num_shifts));
        return num_shifts >= num_residues - 1;
    else: #even X --> impossible unless X=2,R=1
        return R == 1;
    
def xomino(filename):
    IN = open(filename, 'r');
    OUT = open(filename[:filename.find('.')] + '.out', 'w');
    num_cases = int(IN.readline());
    for case in range(1, num_cases+1):
        line = IN.readline();
        X,R,C = map(int, line.split(' '));
        if canTile(X,R,C):
            OUT.write("Case #%d: GABRIEL" % (case))
        else: OUT.write("Case #%d: RICHARD" % (case))
        if (case != num_cases): OUT.write('\n');
        

if __name__ == "__main__":
    import sys;
    xomino(sys.argv[1]);