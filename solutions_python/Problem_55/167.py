from numpy import *

FILE = open("C-small.in","r");

def Periodic(k,N,g):
    c = 1;          n0 = 0;         seats = [];     Gstart = zeros(N);
    Money = 0;      Tstart = 0;     Tend = 0;       Mperiod = 0;
    while (Gstart[n0] <= 3):            # First #2 starts period, #3 ends it.
        if (Gstart[n0] == 1 == max(Gstart)):
            Tstart = c;
        if (Gstart[n0] == 2 == max(Gstart)):
            Tend = c;
            return [(Tend-Tstart), Mperiod];

        Gstart[n0] += 1;
        while ((sum(seats)+g[n0] <= k) and (len(seats) < N)):
            Money += g[n0];
            if (Tstart > 0):
                Mperiod += g[n0];
            seats.append(g[n0]);
            n0 = (n0+1)%N;
#        print c, seats, sum(seats);
        seats = [];
        c += 1;

    print "Um, this should not happen";
    return;


def Header(R,k,N,g):
    c = 1;          n0 = 0;         seats = [];     Money = 0;
    while (c <= R):
        while ((sum(seats)+g[n0] <= k) and (len(seats) < N)):
            Money += g[n0];
            seats.append(g[n0]);
            n0 = (n0+1)%N;
        seats = [];
        c += 1;
    return Money


def Solve(R,k,N, g):
    [T, MoneyT] = Periodic(k,N,g);

    Head = R - (R/T-2)*T;
    if (Head > R):
        Head = R;
    Periods = (R-Head)/T;

    R = Periods*MoneyT + Header(Head,k,N,g);
    return R;    


T = int(FILE.readline());
for k in range(T):          # Each of the N cases:
    print "Case #%d:" %(k+1),
    [R,k,N] = map(int, FILE.readline().split() );
    g = map( int, FILE.readline().split() );
    print Solve(R,k,N,g);

