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
#define pii pair<int,int>
typedef long long ll;
const int mod = 1000000007;
const int MAXN=105;
const double eps=1e-9;
const int INF=0x3f3f3f3f;
char s[105];
int num[105];
int main()
{
#ifdef LOCAL
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif // LOCAL

    int t;
    scand(t);
    int cas =0;
    while(t--)
    {
        printf("Case #%d: ",++cas);
        scans(s+1);
        int n=strlen(s+1);
        for(int i=1; i<=n; ++i)num[i]=s[i]-'0';
        bool check =1;
        while(check)
        {
            check=0;
            for(int i=2; i<=n; ++i)
            {
                while(num[i]<0)
                {
                    num[i]+=10;
                    num[i-1]--;
                }
                if(num[i]<num[i-1])
                {
                    check=1;
                    num[i]=9;
                    num[i-1]--;
                    for(int j=i; j<=n; ++j)num[j]=9;
                }
            }
        }
        bool ok=0;
        for(int i=1; i<=n; ++i)
        {
            if(num[i])ok=1;
            if(ok)printf("%d",num[i]);
        }
        puts("");
    }
    return 0;
}
