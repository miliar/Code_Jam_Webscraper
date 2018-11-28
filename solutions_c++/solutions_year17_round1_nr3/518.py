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

int Ah,Aa,Bh,Ba;
int B,D;

int ans;
int dp[105][105][105][105];

queue< pair<pii,pii> > Q;

inline pair< pair<int,int> , pair<int,int> > Make(int a,int b,int c,int d)
{
    return mk(mk(a,b),mk(c,d));
}
int BFS()
{
    while(!Q.empty()) Q.pop();
    memset(dp,0x3f,sizeof(dp));
//    cout <<Ah <<" " <<Aa <<" " <<Bh <<" " <<Ba <<endl;
    dp[Ah][Aa][Bh][Ba]=0;
    Q.push(mk(mk(Ah,Aa),mk(Bh,Ba)));
    int a,b,c,d;
    pair< pair<int,int> , pair<int,int> > temp;
    while(!Q.empty())
    {
        temp=Q.front(); Q.pop();
        a=temp.fi.fi;
        b=temp.fi.se;
        c=temp.se.fi;
        d=temp.se.se;
        if(c-b<=0)
        {
            return dp[a][b][c][d]+1;
        }
        if(a-d>0 && dp[a-d][b][c-b][d]==INF)
        {
            dp[a-d][b][c-b][d]=dp[a][b][c][d]+1;
            Q.push(Make(a-d,b,c-b,d));
        }
        if(Ah-d>0 && dp[Ah-d][b][c][d]==INF)
        {
            dp[Ah-d][b][c][d]=dp[a][b][c][d]+1;
            Q.push(Make(Ah-d,b,c,d));
        }
        if(b<c && a-d>0 && dp[a-d][min(b+B,c)][c][d]==INF)
        {
            dp[a-d][min(b+B,c)][c][d]=dp[a][b][c][d]+1;
            Q.push(Make(a-d,min(b+B,c),c,d));
        }
        int td=max(0,d-D);
        if(d>0 && a-td>0 && dp[a-td][b][c][td]==INF)
        {
            dp[a-td][b][c][td]=dp[a][b][c][d]+1;
            Q.push(Make(a-td,b,c,td));
        }
    }
    return INF;
}

void work()
{
    int tc; read(tc);
    int T_T=0;
    while(tc--)
    {
        read(Ah), read(Aa), read(Bh), read(Ba);
        read(B), read(D);

        int ans=BFS();
//        cout <<ans <<endl;

        printf("Case #%d: ",++T_T);
        if(ans==INF) puts("IMPOSSIBLE");
        else printf("%d\n",ans);

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
