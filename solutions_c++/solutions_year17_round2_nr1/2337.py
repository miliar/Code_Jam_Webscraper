#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <queue>
#include <cstdio>
#include <map>
#include <set>
#include <utility>
#include <stack>
#include <cstring>
#include <cmath>
#include <vector>
using namespace std;
#define pb push_back
#define scand(n) scanf("%d",&n)
#define scandd(n,m) scanf("%d%d",&n,&m)
#define scanddd(n,m,k) scanf("%d%d%d",&n,&m,&k)
#define scanlld(n) scanf("%lld",&n)
#define scanlldd(n,m) scanf("%lld%lld",&n,&m)
#define scanllddd(n,m,k) scanf("%lld%lld%lld",&n,&m,&k)
#define scanlf(n) scanf("%lf",&n)
#define scanlff(n,m) scanf("%lf%lf",&n,&m)
#define scanlfff(n,m,k) scanf("%lf%lf%lf",&n,&m,&k)
#define scans(str) scanf("%s",str)
#define ans() printf("%d",ans)
#define ansn() printf("%d\n",ans)
#define anss() printf("%d ",ans)
#define llans() printf("%lld",ans)
#define llanss() printf("%lld ",ans)
#define llansn() printf("%lld\n",ans)
#define REP(i,n) for(int i=0;i<(n);++i)
#define REA(i,qwe,ewr) for(int i=qwe;i<=ewr;++i)
#define RER(i,qwe,ewr) for(int i=qwe;i>=ewr;--i)
#define mst(abc,bca) memset(abc,bca,sizeof abc)
#define all(a) a.begin(),a.end()
#define pii pair<int,int>
typedef long long ll;
inline int mul_mod(int a, int b, int mo)
{
    int ret;
    __asm__ __volatile__ ("\tmull %%ebx\n\tdivl %%ecx\n" : "=d"(ret):"a"(a),"b"(b),"c"(mo));
    return ret;
}
const int mod = 1000000007;
const double eps=1e-9;
const int INF=0x3f3f3f3f;
const int MAXN=100005;


int main()
{
#ifdef LOCAL
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif // LOCAL

    int t;
    scand(t);
    int cas=0;
    while(t--)
    {
        printf("Case #%d: ",++cas);
        int d,n;
        scandd(d,n);
        double ans = 1e9;
        double t=0;
        for(int i=1;i<=n;++i)
        {
            int k,s;
            scandd(k,s);
            t = max(t,1.0*(d-k)/s);
        }
        ans = d/t;
        printf("%.10f\n",ans);
    }
    return 0;
}
