#include <bits/stdc++.h>
using namespace std;
#define fin "GCJ17C3.in"
#define fou "GCJ17C3.out"
#define ff(i, a, b) for(int i = a; i <= b; i ++)
#define fd(i, a, b) for(int i = a; i >= b; i --)
#define x first
#define y second
#define endl '\n'
typedef long long data;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int test;
data n, k;

void read()
{
    cin >> n >> k;
}

void solve(int Tnumber)
{
    cout << "Case #" << Tnumber << ": ";
    data Asize = n, Bsize = 0, Anum = 1, Bnum = 0, m;

    while (k > 0)
    {
        //cerr << k << " " << Asize << " " << Anum << " " << Bsize << " " << Bnum << endl;
        //if (k == 1) exit(0);
        if (k <= Anum)
        {
            m = (Asize + 1) >> 1;
            cout << Asize - m << " " << m - 1 << '\n';
            return;
        }
        else if (k <= Anum + Bnum)
        {
            m = (Bsize + 1) >> 1;
            cout << Bsize - m << " " << m - 1 << '\n';
            return;
        }
        else {
            if (Bnum)
            {
                k -= Anum + Bnum;
                data Am = (Asize + 1) >> 1;
                data Bm = (Bsize + 1) >> 1;
                data Atmp = 0, Btmp = 0;
                data Al = Asize - Am, Ar = Am - 1;
                data Bl = Bsize - Bm, Br = Bm - 1;
                data Smax = max(max(Al, Ar), max(Bl, Br)), Smin = min(min(Al, Ar), min(Bl, Br));
                if (Al == Smax) Atmp += Anum; else Btmp += Anum;
                if (Ar == Smax) Atmp += Anum; else Btmp += Anum;
                if (Bl == Smax) Atmp += Bnum; else Btmp += Bnum;
                if (Br == Smax) Atmp += Bnum; else Btmp += Bnum;
                Asize = Smax, Anum = Atmp;
                Bsize = Bnum = 0;
                if (Smax > Smin) Bsize = Smin, Bnum = Btmp;
            }
            else {
                k -= Anum;
                data Am = (Asize + 1) >> 1;
                data Atmp = 0, Btmp = 0, Al = Asize - Am, Ar = Am - 1;
                data Smax = max(Al, Ar), Smin = min(Al, Ar);
                if (Al == Smax) Atmp += Anum; else Btmp += Anum;
                if (Ar == Smax) Atmp += Anum; else Btmp += Anum;
                Asize = Smax, Anum = Atmp;
                Bsize = Bnum = 0;
                if (Smax > Smin) Bsize = Smin, Bnum = Btmp;
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    //freopen(fin,"r",stdin), freopen(fou,"w",stdout);

    cin >> test;
    ff(i, 1, test)
    {
        read();
        solve(i);
    }
    return 0;
}
