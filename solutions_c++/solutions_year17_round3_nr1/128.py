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
        vector<PLL> p(n);
        REP(i,n)
        {
            LL r,h;
            cin>>r>>h;
            p[i]=PLL(2*r*h,r);
        }
        sort(ALL(p),greater<PLL>());
        LL ss=0;
        REP(i,k-1)
            ss+=p[i].first;
        LL ans=0;
        REP(i,n)
        {
            if(i<k-1)
            {
                ans=max(ans,ss+p[k-1].first+p[i].second*p[i].second);
            }
            else
            {
                ans=max(ans,ss+p[i].first+p[i].second*p[i].second);
            }
        }
        //cout<<ans<<endl;
        cout<<"Case #"<<l+1<<": "<<setprecision(8)<<fixed<<ans*pi<<endl;
    }
}