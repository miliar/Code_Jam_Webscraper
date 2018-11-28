#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <limits.h>
#include <assert.h>
#include <math.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <list>
#include <bitset>
#include <vector>
using namespace std;

#define LL long long

#define fi first
#define se second
#define lson l,mid,id<<1
#define rson mid+1,r,id<<1|1
#define ls id<<1
#define rs id<<1|1
#define MID(a,b) (((a)+(b))>>1)
#define maxx(a,b) ((a)<(b)?(b):(a))
#define minx(a,b) ((a)<(b)?(a):(b))
#define absx(a) ((a)<0?-(a):(a))
#define mk(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define itr iterator
#define lowbit(x) ((x)&-(x))

typedef unsigned LL ULL;
typedef unsigned uint;
typedef map<int,int> mii;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef pair<LL,LL> pLL;

template< typename T > inline void read(T &x) {
    bool f=0; char ch=getchar(); x=0;
    while(ch<'0' || ch>'9') {if(ch=='-') f=1; ch=getchar();}
    while(ch>='0' && ch<='9') {x=x*10+ch-'0'; ch=getchar();}
    if(f) x=-x;
}

template< typename T > inline void Max(T &a, T b) {if(a<b) a=b;}
template< typename T > inline void Min(T &a, T b) {if(b<a) a=b;}
template< typename T > inline T Abs(T a) {if(a<0) return -a; else return a;}

const double pi=(double) acos(-1.0);
const int MOD=(int) 1e9+7;
const int INF=(int) 0x3f3f3f3f;
const LL  LINF=(LL) INF<<32|INF;
const int SINF=(uint) ~0>>1;
const LL  SLINF=(ULL) (-1)>>1;
const double DINF=(double) 1e50;
const double eps=(double) 1e-4;
const int maxn=(int) 1e3+10;
const int maxm=(int) 1e4+10;
const int maxk=(int) 5e2+10;

inline int sig(double x) {return x<-eps?-1:x>eps;}

//--------------start------------------

int n,m;
char Map[105][105],ans[105][105];

struct adjs{int to,next;}ad[105*105];
int head[205], adcnt;
inline void adjs_init() {memset(head,-1,sizeof(head)); adcnt=0;}
inline void add_edge(int from,int to) {ad[adcnt].to=to; ad[adcnt].next=head[from]; head[from]=adcnt++;}
bool vis[205];
int match[205];

bool r[205],c[205];
bool rr[205],cc[205];

bool dfs(int u)
{
    for(int i=head[u];~i;i=ad[i].next)
    {
        int v=ad[i].to;
        if(vis[v]) continue;
        vis[v]=1;
        if(match[v]==-1 || dfs(match[v]))
        {
            match[v]=u;
            return 1;
        }
    }
    return 0;
}

void work()
{
    int tc; read(tc);
    int T_T=0;
    while(tc--)
    {
        memset(Map,'.',sizeof(Map));
        memset(ans,'.',sizeof(ans));

        read(n), read(m);

        for(int i=1;i<=n;i++) r[i]=1, c[i]=1;
        memset(rr,1,sizeof(rr));
        memset(cc,1,sizeof(cc));

        for(int i=0;i<m;i++)
        {
            char s[3]; int x,y;
            scanf("%s%d%d",s,&x,&y);
            ans[x][y]=Map[x][y]=s[0];
            if(s[0]=='o' || s[0]=='x') r[x]=0, c[y]=0;
            if(s[0]=='o' || s[0]=='+') rr[x-y+n]=0, cc[x+y]=0;
        }

        while(1)
        {
            int nx=-1,ny=-1;
            for(int i=1;i<=n;i++)
            {
                if(r[i]) nx=i;
                if(c[i]) ny=i;
            }
            ans[nx][ny] = ans[nx][ny]=='.' ? 'x' : 'o';
            if(nx==-1 || ny==-1) break;
            r[nx]=0; c[ny]=0;
        }

        adjs_init();
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
                if(rr[i-j+n] && cc[i+j])
                    add_edge(i-j+n,i+j);

        memset(match,-1,sizeof(match));

        for(int i=1;i<=2*n-1;i++)
        {
            memset(vis,0,sizeof(vis));
            dfs(i);
        }

        for(int i=2;i<=2*n;i++)
        {
            if(match[i]==-1) continue;
            int u=match[i], v=i;
            u-=n;
            int x=(u+v)/2, y=(v-u)/2;
            ans[x][y] = ans[x][y]=='.' ? '+' : 'o';
        }

        int sco=0, cnt=0;
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
            {
                if(ans[i][j]!=Map[i][j]) cnt++;
                if(ans[i][j]=='o') sco+=2;
                else if(ans[i][j]!='.') sco++;
            }

        printf("Case #%d: ",++T_T);
        printf("%d %d\n",sco,cnt);

        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
                if(ans[i][j]!=Map[i][j])
                    printf("%c %d %d\n",ans[i][j],i,j);
    }
}

//--------------end--------------------

//#define yukihana0416
int main()
{
#ifdef yukihana0416
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
#endif // yukihana0416
    work();
    return 0;
}
