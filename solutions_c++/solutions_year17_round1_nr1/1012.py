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
const int MOD=(int) 1e7+9;
const int INF=(int) 0x3f3f3f3f;
const LL  LINF=(LL) INF<<32|INF;
const int SINF=(uint) ~0>>1;
const LL  SLINF=(ULL) (-1)>>1;
const double DINF=(double) 1e50;
const double eps=(double) 1e-4;
const int maxn=(int) 5e5+10;
const int maxm=(int) 1e4+10;
const int maxk=(int) 5e2+10;

inline int sig(double x) {return x<-eps?-1:x>eps;}

//--------------start------------------

int n,m;
char str[30][30];
bool vis[30][30];

inline bool check_c(int c,int x,int y)
{
    bool res=1;
    for(int i=x;i<=y;i++) if(str[i][c]!='?') res=0;
    return res;
}

inline bool check_r(int r,int x,int y)
{
    bool res=1;
    for(int i=x;i<=y;i++) if(str[r][i]!='?') res=0;
    return res;
}

void work()
{
    int tc; read(tc);
    int T_T=0;
    while(tc--)
    {
        read(n), read(m);
        memset(vis,0,sizeof(vis));
        for(int i=1;i<=n;i++)
            scanf("%s",str[i]+1);

//        for(int i=1;i<=n;i++)
//        {
//            for(int j=1;j<=m;j++)
//                putchar(str[i][j]);
//            puts("");
//        }

        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++)
                if(str[i][j]!='?' && !vis[i][j])
                {
                    char c=str[i][j];
                    int l=j, r=j;
                    while(l-1>=1)
                    {
                        if(str[i][l-1]!='?') break;
                        l--;
                    }
                    while(r+1<=m)
                    {
                        if(str[i][r+1]!='?') break;
                        r++;
                    }

                    int u=i, d=i;
                    while(u-1>=1)
                    {
                        if(check_r(u-1,l,r)==0) break;
                        u--;
                    }
                    while(d+1<=n)
                    {
                        if(check_r(d+1,l,r)==0) break;
                        d++;
                    }

                    for(int i=u;i<=d;i++)
                        for(int j=l;j<=r;j++)
                            str[i][j]=c, vis[i][j]=1;

                }

        printf("Case #%d:\n",++T_T);
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
                putchar(str[i][j]);
            putchar('\n');
        }
    }
}

//--------------end--------------------

int main()
{
#ifdef yukihana0416
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
#endif // yukihana0416
    work();
    return 0;
}
