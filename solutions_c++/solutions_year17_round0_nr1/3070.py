#include <bits/stdc++.h>

#ifndef LOCAL
#define cerr dolor_sit_amet
#endif

#define mp make_pair
//#define sz(x) ((int)((x).size()))
#define X first
#define Y second

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair < int , int > ipair;
typedef pair < ll , ll > lpair;
const int IINF = 0x3f3f3f3f;
const ll LINF = 0x3f3f3f3f3f3f3f3fll;
const double DINF = numeric_limits<double>::infinity();
const ll MOD = 1000000007;
const double EPS = 1e-9;
const int DX[] = { 1,  0, -1,  0,  1, -1,  1, -1};
const int DY[] = { 0,  1,  0, -1,  1, -1, -1,  1};
int manhattan(ipair a, ipair b)
{
    return abs(a.X-b.X)+abs(a.Y-b.Y);
}
ifstream fin("data.in");
ofstream fout("data.out");
int main()
{
    int n,t,i,j,fli,rez;
    char c[1003];
    bool v[1003];
    fin>>t;
    for(int caz=1;caz<=t;caz++)
    {
        fin>>c>>fli;
        n=strlen(c);
//        cout<<c<<'c';
        for(i=1;i<=n;i++)
            v[i]=!((c[i-1]&4)>>2);
        rez=0;
        for(i=1;i<=n;i++)
        {
            if(!v[i])
            {
                if(i+fli-1>n)
                {
                    rez=-1;
                    break;
                }
                ++rez;
                for(j=i;j<=i+fli-1;j++)
                {
                    v[j]^=1;
                }
            }
        }
//        cout<<rez<<'\n';
        if(rez==-1)
            fout<<"Case #"<<caz<<": IMPOSSIBLE\n";
        else
            fout<<"Case #"<<caz<<": "<<rez<<"\n";

    }
    return 0;
}
