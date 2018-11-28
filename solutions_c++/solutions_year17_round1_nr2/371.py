#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <cmath>
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
int T,n,p;
const int maxn = 105;
int q[maxn][maxn];
int pp[maxn];
int R[maxn];
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> T;
    int cas = 0;
    while(T--){
 
        cin>>n>>p;
        fori cin >> R[i];
        fori {FOR(j,p) cin >> q[i][j]; sort(q[i]+1,q[i]+1+p);}
        fori pp[i]=1;
        
        int ans = 0;
        for(int s=1;s<=5000000;s++){
            bool flag = true;
            fori{
                LL d=ceil(0.9*s*R[i]);  LL dd = floor(1.1*s*R[i]);
                while(pp[i] <= p && q[i][pp[i]]<d) pp[i]++;
                if(q[i][pp[i]] > dd || pp[i] > p) flag = false;
            }
            if(flag){
                ans++;
                s--;
                fori pp[i]++;
            }
            bool f = false;
            fori if(pp[i]>p) f=true;
            if(f) break;
        }
        printf("Case #%d: ",++cas);
        cout<<ans<<endl;
    }
    return 0;
}
