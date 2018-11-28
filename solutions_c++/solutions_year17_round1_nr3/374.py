#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <cmath>
#include <map>
using namespace std;
#define read freopen("in.txt","r",stdin)
#define maxlongint 2147483647
typedef  long long LL;
typedef  unsigned long long ULL;
#pragma comment(linker, "/STACK:102400000,102400000")
#define fori for(int i=1;i<=n;i++)
#define forj for(int j=1;j<=n;j++)
#define fork for(int k=1;k<=n;k++)
#define FOR(i,n) for(int i=1;i<=n;i++)
#define REP(i,a,b) for(int i=a;i<=b;i++)
#define DREP(i,a,b) for(int i=a;i>=b;i--)
#define DOWN(i,n) for(int i=n;i>=1;i--)
#define enter cout<<endl;
#define in push_back
#define out pop_back
#define sqr(x) ((x)*(x))
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define offcin ios::sync_with_stdio(false)
#define s(n) scanf("%d",&n)
#define sll(n) scanf("%lld",&n)
#define sd(x,y) scanf("%d%d",&x,&y)
#define sch(s) scanf("%s",s)
#define fillfalse(v) memset(v,false,sizeof(v))
#define filltrue(v) memset(v,true,sizeof(v))
#define f0(a)    memset(a,0,sizeof(a))
#define Fillplus(a)    memset(a,-1,sizeof(a))
#define lowbit(x) x&(-x)
using namespace std;

struct app{
    int h1, h2, a1, a2;
    friend bool operator<(const app& x, const app& y) {
        auto t1 = make_pair(make_pair(x.h1, x.h2), make_pair(x.a1, x.a2));
        auto t2 = make_pair(make_pair(y.h1, y.h2), make_pair(y.a1, y.a2));
        return t1 < t2;
    }
};
map<app,int> mp;
int main() {
    int T;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    int cas=0;
    while(T--) {
        
        int hd, ad, hk, ak, b, d;
        cin >> hd >> ad >> hk >> ak >> b >> d;
        mp.clear();
        mp[app{hd, hk, ad, ak}] = 1;
        queue<app> q;
        q.push(app{hd, hk, ad, ak});
        int ans = -1;
        while (!q.empty()) {
            app x = q.front();
            q.pop();
            app y = x;
            y.h2 -= y.a1;
            if (y.h2 <= 0) {
                ans = mp[x] + 1;
                break;
            }
            y.h1 -= y.a2;
            if (y.h1 > 0 && !mp[y]) {
                mp[y]=mp[x];
                mp[y]++;
                q.push(y);
            }
            
            y = x;
            y.a1 += b;
            y.h1 -= y.a2;
            if (y.h1 > 0 && !mp[y]) {
                mp[y]=mp[x];
                mp[y]++;
                q.push(y);
            }
            
            y = x;
            y.h1 = hd;
            y.h1 -= y.a2;
            if (y.h1 > 0 && !mp[y]) {
                mp[y]=mp[x];
                mp[y]++;
                q.push(y);
            }
            
            y = x;
            y.a2 -= d;
            y.a2 = max(y.a2, 0);
            y.h1 -= y.a2;
            if (y.h1 > 0 && !mp[y]) {
                mp[y]=mp[x];
                mp[y]++;
                q.push(y);
            }
        }
        printf("Case #%d: ", ++cas);
        if(ans==-1) printf("IMPOSSIBLE\n");
           else printf("%d\n",ans-1);
    }
    return 0;
}
