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
const LD pi=3.141592653589793238462643383279502884;


int main()
{
    int tt;
    cin>>tt;
    REP(l,tt)
    {
        int n,k;
        cin>>n>>k;
        double u;
        cin>>u;
        vector<double> p(n+1);
        REP(i,n)
            cin>>p[i];
        p[n]=1;
        sort(ALL(p));
        FOR(i,1,n+1)
        {
            if((p[i]-p[i-1])*i<=u)
            {
                u-=(p[i]-p[i-1])*i;
                REP(j,i)
                    p[j]=p[i];
            }
            else
            {
                REP(j,i)
                    p[j]+=u/i;
                break;
            }
        }
        LD ans=1;
        REP(i,n)
            ans*=p[i];

        cout<<"Case #"<<l+1<<": "<<setprecision(10)<<fixed<<ans<<endl;
    }
}