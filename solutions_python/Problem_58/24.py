from numpy import *

FILE = open("C-small.in","r");


def Solve(A,B):       # move is 1 for A, 2 for B
    Moves = 0;      N = [max(A,B), min(A,B)];      

#    print (A,B);

    A = N[-2];     B = N[-1];
    if (A == B):        # Player to move has to love
        return False;
    if (A*B == 0):        # Player to move has already won
        return True;

#    print (A,B);
    k = (A/B);
    
    if (k == 1):
        Moves += 1;
        return (not Solve(B,A-k*B));
    if (Moves == 0):
        return (Solve(B,A-k*B) or Solve(B, A-(k-1)*B));
    if (Moves == 1):
        return not((Solve(B,A-k*B) or  Solve(B, A-(k-1)*B)));
        

T = int(FILE.readline());
for k in range(T):          # Each of the N cases:
    print "Case #%d:" %(k+1),
    [A1,A2,B1,B2] = map( int, FILE.readline().split() );
    Ans = 0;
    for A in range(A1,A2+1):
        for B in range(B1, B2+1):
            Ans += int(Solve(A,B));
    print Ans;
