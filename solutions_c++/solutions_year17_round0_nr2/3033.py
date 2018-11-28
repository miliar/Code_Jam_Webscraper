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

        int t,i,caz,n;
        char c[100];

        fin>>t;
        for(caz=1;caz<=t;caz++)
        {
            int poz,pozinit=0,ok=0;
            fin>>c;
            n=strlen(c);
            poz=n-1;
            while(!ok)
            {
                ok=1;
                for(i=0;i<n-1;i++)
                {
                    if(c[i]>c[i+1])
                    {
                        poz=min(i,poz);
                        --c[i];
                        c[i+1]='9';
                        ok=0;
                        break;

                    }
                }
            }
            fout<<"Case #"<<caz<<": ";
            if(c[0]=='0')
                pozinit=1;
            for(i=pozinit;i<=poz;i++)
                fout<<c[i];
            for(;i<n;i++)
                fout<<"9";
            fout<<'\n';

        }


//            fout<<"Case #"<<caz<<": IMPOSSIBLE\n";
//        else
//            fout<<"Case #"<<caz<<": "<<rez<<"\n";


    return 0;
}
