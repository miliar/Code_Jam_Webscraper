#include <bits/stdc++.h>
#include <iomanip>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;
typedef long double LD;
typedef pair<LD, LD> PLDLD;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
#define CLR(a) memset((a), 0 ,sizeof(a))
#define ALL(a) a.begin(),a.end()

const double eps=1e-5;
const LL INF=1e15;

int main()
{
    int t;
    cin>>t;
    REP(tt,t)
    {
        int n,d;
        cin>>d>>n;
        double minspeed=0;
        REP(i,n)
        {
            int kk,k,s;
            cin>>kk>>s;
            k=d-kk;
            minspeed=max(minspeed, (double)k/s);
        }

        cout<<setprecision(10)<<fixed
        <<"Case #"<<tt+1<<": "<<d/minspeed<<endl;


    }

}